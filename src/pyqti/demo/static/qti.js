// Front-end for the pyqti demo.
//
// The server renders qti-choice-interaction / qti-simple-choice through as real
// custom elements, so this file is the seam the README's "web components for the
// qti-item-body" approach needs. A React implementation later replaces the element
// definition below; the HTML contract and the JSON contract stay exactly as they are.

class QtiChoiceInteraction extends HTMLElement {
  connectedCallback() {
    if (this._upgraded) return;
    this._upgraded = true;

    this.responseIdentifier = this.getAttribute("response-identifier");
    this.maxChoices = parseInt(this.getAttribute("max-choices") ?? "1", 10);
    this.minChoices = parseInt(this.getAttribute("min-choices") ?? "0", 10);

    // max-choices="1" is single cardinality -> radio. Anything else is a
    // multi-select, which pyqti does not grade yet; the input type still reflects
    // the item so the mismatch is visible rather than silent.
    const inputType = this.maxChoices === 1 ? "radio" : "checkbox";

    const prompt = this.querySelector(":scope > qti-prompt");
    const choices = Array.from(this.querySelectorAll(":scope > qti-simple-choice"));

    const fieldset = document.createElement("fieldset");
    fieldset.className = "qti-choices";
    fieldset.dataset.orientation = this.getAttribute("orientation") ?? "vertical";

    const legend = document.createElement("legend");
    legend.innerHTML = prompt ? prompt.innerHTML : "Choose one";
    fieldset.appendChild(legend);

    for (const choice of choices) {
      const identifier = choice.getAttribute("identifier");
      const id = `${this.responseIdentifier}-${identifier}`;

      const label = document.createElement("label");
      label.className = "qti-choice";
      label.setAttribute("for", id);

      const input = document.createElement("input");
      input.type = inputType;
      input.name = this.responseIdentifier;
      input.value = identifier;
      input.id = id;

      const text = document.createElement("span");
      text.innerHTML = choice.innerHTML;

      label.append(input, text);
      fieldset.appendChild(label);
    }

    if (prompt) prompt.remove();
    for (const choice of choices) choice.remove();
    this.appendChild(fieldset);
  }

  // Single cardinality yields a scalar (or null); multiple yields an array. This
  // mirrors the JSON encoding rules the server documents.
  get value() {
    const checked = Array.from(
      this.querySelectorAll("input:checked"),
      (input) => input.value,
    );
    if (this.maxChoices === 1) {
      return checked.length ? checked[0] : null;
    }
    return checked;
  }
}

customElements.define("qti-choice-interaction", QtiChoiceInteraction);

function collectResponses(form) {
  const responses = {};
  for (const interaction of form.querySelectorAll("qti-choice-interaction")) {
    responses[interaction.responseIdentifier] = interaction.value;
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
        body: JSON.stringify({ responses: collectResponses(form) }),
      });
      renderResult(output, await response.json());
    } catch (err) {
      renderResult(output, {
        error: { type: "NetworkError", message: String(err) },
      });
    }
  });
});
