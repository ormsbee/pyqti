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
    fetch(scoreUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ responses: collectResponses() }),
    })
      .then(function (response) {
        return response.json();
      })
      .then(render)
      .catch(function () {
        render({ error: "Could not reach the server." });
      })
      .then(function () {
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

  root.addEventListener("click", function (event) {
    if (!event.target.classList.contains("pyqti-studio-save")) {
      return;
    }
    event.preventDefault();
    if (errorBox) {
      errorBox.hidden = true;
    }
    runtime.notify("save", { state: "start" });
    fetch(saveUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ values: { qti_xml: textarea.value } }),
    })
      .then(function (response) {
        return response.json().then(function (body) {
          return { ok: response.ok, body: body };
        });
      })
      .then(function (result) {
        if (!result.ok) {
          runtime.notify("error", { title: "Could not save", message: "" });
          // The author gets pyqti's own message verbatim: it names the field or
          // rule at fault, which a paraphrase would lose.
          showError((result.body && result.body.error) || "Invalid QTI.");
          return;
        }
        runtime.notify("save", { state: "end" });
      })
      .catch(function () {
        showError("Could not reach the server.");
      });
  });
}
