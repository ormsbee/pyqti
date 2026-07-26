// Glue between Citolab's QTI web components and pyqti's grading endpoint.
//
// This file deliberately contains no rendering and no scoring. Citolab renders the
// item from the XML pyqti serves; pyqti scores the responses. All this does is move
// candidate responses from the former to the latter.
//
// Note what is NOT here: nothing invokes Citolab's response-processing entry point,
// and nothing displays a correct response. The served XML contains neither response
// processing nor a correct response, so there is nothing to evaluate or reveal even
// by accident.

const CONTEXT_UPDATED = "qti-item-context-updated";

// Response variables live alongside outcome and built-in variables in the item
// context. Only responses may be sent: the server derives outcomes itself and
// ignores anything else, but there is no reason to put them on the wire.
const NOT_RESPONSES = new Set([
  "completionStatus",
  "numAttempts",
  "duration",
  "SCORE",
  "MAXSCORE",
  "FEEDBACK",
]);

let latestVariables = [];

document.addEventListener(CONTEXT_UPDATED, (event) => {
  latestVariables = event.detail?.itemContext?.variables ?? [];
});

function collectResponses() {
  const responses = {};

  // Prefer reading straight off the element: it is authoritative at submit time,
  // whereas the event only tells us about the last change.
  const item = document.querySelector("qti-assessment-item");
  const variables = item?.variables ?? latestVariables;

  for (const variable of variables) {
    const identifier = variable.identifier;
    if (!identifier || NOT_RESPONSES.has(identifier)) continue;
    // Citolab reports declared-but-unset variables too; null is a NULL response,
    // which pyqti handles, so pass it through rather than dropping the key.
    responses[identifier] = variable.value ?? null;
  }
  return responses;
}

function renderResult(output, data) {
  output.hidden = false;

  if (data.error) {
    output.className = "error";
    output.textContent = `${data.error.type}: ${data.error.message}`;
    return;
  }

  const outcomes = Object.entries(data.outcomes)
    .map(([key, value]) => `${key} = ${JSON.stringify(value)}`)
    .join(", ");

  output.className = data.valid ? "ok" : "warn";
  const problems = data.errors.length ? ` (${data.errors.join("; ")})` : "";
  output.textContent = `${outcomes} [${data.completion_status}]${problems}`;
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("qti-form");
  if (!form) return;
  const output = document.getElementById("qti-result");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(form.dataset.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ responses: collectResponses() }),
      });
      renderResult(output, await response.json());
    } catch (err) {
      renderResult(output, {
        error: { type: "NetworkError", message: String(err) },
      });
    }
  });
});
