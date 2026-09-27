/* Glue between Citolab's QTI web components and this XBlock's handlers.
 *
 * As in the demo harness, this file contains no rendering and no scoring.
 * Citolab renders from the redacted XML the block serves; pyqti scores, on the
 * server, against the item the browser never sees. Note what is NOT here:
 * nothing imports Citolab's response-processing module and nothing calls
 * processResponse(), so there is no client-side scoring path to disagree with
 * the server's, even by accident.
 *
 * Everything is scoped to the block's own `element`. The demo could get away
 * with document-level lookups and fixed ids; a unit page may hold several of
 * these, and document-level anything would cross-wire them.
 */

var pyqtiComponentsLoaded = {};

function pyqtiLoadComponents(baseUrl) {
  if (!pyqtiComponentsLoaded[baseUrl]) {
    // Dynamic import() works from a classic script, which is what the XBlock
    // fragment pipeline gives us; a <script type="module"> injected as fragment
    // content would not reliably execute.
    pyqtiComponentsLoaded[baseUrl] = Promise.all([
      import(baseUrl + "/qti-item/+esm"),
      import(baseUrl + "/qti-elements/+esm"),
      import(baseUrl + "/qti-interactions/+esm"),
    ]);
  }
  return pyqtiComponentsLoaded[baseUrl];
}

// Open edX enforces CSRF on handler POSTs: Studio through Django's middleware,
// the LMS explicitly for session-authenticated users. The platform adds the
// token to jQuery requests via $.ajaxSetup, which fetch() never sees, so the
// header has to be sent here. `csrftoken` is the cookie that setup reads too.
function pyqtiCsrfToken() {
  var match = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]*)/);
  return match ? decodeURIComponent(match[1]) : "";
}

function pyqtiPostJson(url, payload) {
  return fetch(url, {
    method: "POST",
    credentials: "same-origin",
    // Handlers never redirect, but the platform does when the session has
    // expired, to a login page that may be on another origin. Following it
    // would surface as a network failure, or as a 200 page of HTML.
    redirect: "manual",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": pyqtiCsrfToken(),
    },
    body: JSON.stringify(payload),
  });
}

// The block's handlers always answer in JSON, errors included. Anything else
// came from the platform in front of them -- a CSRF rejection, a login
// redirect, a proxy's error page -- and is still a server response, so it must
// not be reported as a network failure, nor a 200 of HTML as success.
function pyqtiReadResponse(response) {
  return response.text().then(function (text) {
    var body = null;
    try {
      body = JSON.parse(text);
    } catch (error) {
      body = null;
    }
    return {
      ok: response.ok && body !== null,
      status: response.status,
      redirected: response.type === "opaqueredirect",
      body: body,
    };
  });
}

function pyqtiErrorMessage(result) {
  // A handler's own message is passed on verbatim: pyqti's name the field or
  // rule at fault, which a paraphrase would lose.
  if (result.body && typeof result.body.error === "string") {
    return result.body.error;
  }
  if (result.redirected || result.status === 403) {
    return (
      "The server refused the request. Your session may have expired: " +
      "reload the page and try again."
    );
  }
  return "The server sent an unexpected response (HTTP " + result.status + ").";
}

// Response variables share the item context with outcome and built-in
// variables. Only responses may go on the wire: the server derives outcomes
// itself and ignores anything else.
var PYQTI_NOT_RESPONSES = [
  "completionStatus",
  "numAttempts",
  "duration",
  "SCORE",
  "MAXSCORE",
  "FEEDBACK",
];

function QtiAssessmentItemBlock(runtime, element, initArgs) {
  var args = initArgs || {};
  var root = element.querySelector ? element : element[0];
  var form = root.querySelector(".pyqti-form");
  var output = root.querySelector(".pyqti-result");
  var submit = root.querySelector(".pyqti-submit");
  var container = root.querySelector("item-container");
  if (!form || !container) {
    return;
  }

  var itemUrl = runtime.handlerUrl(element, "item_xml");
  var scoreUrl = runtime.handlerUrl(element, "submit_response");
  var latestVariables = [];

  // Scoped to the block, not the document: two items on one page must not see
  // each other's responses.
  root.addEventListener("qti-item-context-updated", function (event) {
    var detail = event.detail || {};
    latestVariables = (detail.itemContext && detail.itemContext.variables) || [];
  });

  function findAssessmentItem() {
    // item-container renders into its own (open) shadow root, so a light-DOM
    // query alone never finds the item.
    var shadow = container.shadowRoot;
    return (
      (shadow && shadow.querySelector("qti-assessment-item")) ||
      root.querySelector("qti-assessment-item")
    );
  }

  function collectResponses() {
    var item = findAssessmentItem();
    var variables = (item && item.variables) || latestVariables || [];
    var responses = {};
    variables.forEach(function (variable) {
      if (PYQTI_NOT_RESPONSES.indexOf(variable.identifier) !== -1) {
        return;
      }
      responses[variable.identifier] =
        variable.value === undefined ? null : variable.value;
    });
    return responses;
  }

  function render(data) {
    if (!output) {
      return;
    }
    output.hidden = false;
    if (data.error) {
      output.className = "pyqti-result error";
      output.textContent = data.error;
      return;
    }
    var parts = [];
    if (data.score !== undefined) {
      parts.push(data.score + " / " + data.max_score);
    } else {
      parts.push("Response recorded.");
    }
    if (data.errors && data.errors.length) {
      parts.push("(" + data.errors.join("; ") + ")");
    }
    if (data.attempts_remaining !== null && data.attempts_remaining !== undefined) {
      parts.push("[" + data.attempts_remaining + " attempts left]");
    }
    output.className = data.valid ? "pyqti-result ok" : "pyqti-result warn";
    output.textContent = parts.join(" ");
  }

  pyqtiLoadComponents(args.componentsUrl).then(function () {
    // Set the seed on the element, not on a page global: the seed is derived
    // per learner *and per usage*, so two blocks on a page need different ones.
    if (args.seed) {
      container.qtiContext = { QTI_CONTEXT: { seed: args.seed } };
    }
    container.setAttribute("item-url", itemUrl);
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (submit) {
      submit.disabled = true;
    }
    pyqtiPostJson(scoreUrl, { responses: collectResponses() })
      .then(pyqtiReadResponse)
      .then(
        function (result) {
          render(result.ok ? result.body : { error: pyqtiErrorMessage(result) });
        },
        function () {
          render({ error: "Could not reach the server." });
        }
      )
      .finally(function () {
        if (submit) {
          submit.disabled = false;
        }
      });
  });
}

function QtiAssessmentItemStudio(runtime, element) {
  var root = element.querySelector ? element : element[0];
  var textarea = root.querySelector(".pyqti-xml");
  var errorBox = root.querySelector(".pyqti-studio-error");
  var saveUrl = runtime.handlerUrl(element, "submit_studio_edits");

  function showError(message) {
    if (!errorBox) {
      return;
    }
    errorBox.hidden = false;
    errorBox.textContent = message;
  }

  function fail(message) {
    // Studio ignores an error notify with no message. Given one, it takes the
    // place of the "Saving" notification, which otherwise stays up: the only
    // other way to clear that is "end", which closes the editor as if saved.
    runtime.notify("error", {
      title: "Could not save",
      message: "The item was not saved. The reason is shown in the editor.",
    });
    showError(message);
  }

  root.addEventListener("click", function (event) {
    if (!event.target.classList.contains("pyqti-studio-save")) {
      return;
    }
    event.preventDefault();
    if (errorBox) {
      errorBox.hidden = true;
    }
    runtime.notify("save", { state: "start" });
    pyqtiPostJson(saveUrl, { values: { qti_xml: textarea.value } })
      .then(pyqtiReadResponse)
      .then(
        function (result) {
          if (result.ok) {
            runtime.notify("save", { state: "end" });
          } else {
            fail(pyqtiErrorMessage(result));
          }
        },
        function () {
          fail("Could not reach the server.");
        }
      );
  });
}
