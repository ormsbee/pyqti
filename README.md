# PyQTI

An early implementation of the QTI 3.0 standard for Python.

The first goal is going to be to get simple multiple choice problems to render.

## High Level Approach

Web components for the qti-item-body, Python backend for everything else.

**pyqti does not render.** Presentation is delegated to existing QTI web components
in the browser --- currently [Citolab
`@citolab/qti-components`](https://github.com/Citolab/qti-components), which already
implements the QTI presentation vocabulary and is tested against 1EdTech conformance
items. Those components consume QTI XML directly, so pyqti's job on the presentation
side is to publish a **presentation-safe** copy of the item and keep the
authoritative one to itself. See "Serving items safely" below --- this is the part
that matters, because QTI XML contains the answer.

## Status

Single-answer multiple choice items are delivered and graded end to end. Concretely,
that means a `qti-choice-interaction` with `max-choices="1"`, bound to a `single`
cardinality `identifier` response, graded by real response processing.

**Implemented**

- Parsing `qti-assessment-item` with a deliberately strict parser configuration.
- Serializing models back to QTI XML (`pyqti.serialization`), and deriving a
  redacted, presentation-safe item from one (`pyqti.redaction`).
- A response-processing interpreter covering `qti-response-condition`,
  `qti-response-if` / `-else-if` / `-else`, `qti-set-outcome-value`,
  `qti-exit-response`, and the expressions `qti-variable`, `qti-correct`,
  `qti-base-value`, `qti-null`, `qti-is-null`, `qti-match`, `qti-not`, `qti-and`,
  `qti-or` --- with QTI's three-valued (true/false/NULL) logic.
- Resolution of the built-in response processing templates by URI, from vendored
  copies in `pyqti/processing/templates/`. `match_correct` works; `map_response` is
  vendored but raises until `qti-map-response` is implemented.
- An item session with correct (and asymmetric) variable initialisation.

**Not implemented.** Everything below raises a subclass of `UnsupportedQtiFeature`
rather than being silently ignored --- see "Failing loudly" below: multiple/ordered
cardinality, `MAP_RESPONSE` and `qti-mapping`, `shuffle`, feedback
(`qti-modal-feedback`, `qti-feedback-block`), `template-location`,
`qti-response-processing-fragment`, XInclude, other interaction types, tests and
sections, and template processing. Note that MathML, images and tables now render
fine --- that is the renderer's job, and the renderer is no longer pyqti's.

**Before this is usable for real high-stakes delivery** it also needs: durable
server-side session state and attempt binding; a server-fixed shuffle order (Citolab
accepts a `seed`, so pyqti should supply one per attempt); template processing for
randomised items; and withholding outcomes until score release. The demo returns
scores immediately, which is right for a demo and wrong for an exam.

### Try it

```sh
uv run qti-demo          # then open http://127.0.0.1:8000/
uv run pytest
uv run ruff check && uv run mypy
uv run overhead          # model import / parse memory and timing
```

### Library use

```python
from pathlib import Path
from pyqti import ItemSession, load_assessment_item, presentation_xml

item = load_assessment_item(Path("examples/firstexample.xml"))

xml = presentation_xml(item)           # safe to send to a browser; no answer in it
session = ItemSession(item)            # grades against the authoritative item
session.submit({"RESPONSE": "A"})      # -> {'SCORE': 1.0}
session.submit({"RESPONSE": "B"})      # -> {'SCORE': 0.0}
```

`load_assessment_item` takes XML *content* as `str`/`bytes`, or a file via `Path` or
a file object.

## Serving items safely

A QTI item contains the answer. `qti-correct-response`, `qti-mapping`, inline
`qti-response-processing` and feedback bodies all live in the same document the
renderer needs. Handing a browser the item as authored hands the candidate the answer
key via devtools.

So pyqti holds every item twice. The authoritative copy never leaves the server and is
what `ItemSession` grades against; `presentation_xml()` derives the only copy a
candidate may receive. **It is the only function permitted to produce item XML for a
front end.**

Redaction works from an **allowlist**: every field of `QtiAssessmentItem` is
explicitly classified in `pyqti/redaction.py`, and an unclassified field raises. A
denylist would only remove the leaks somebody already thought of, whereas the real
risk is a QTI feature nobody anticipated. `tests/test_redaction.py` enforces the same
shape on the output — the served XML may only contain elements from a permitted set,
so anything unfamiliar fails the build rather than reaching a candidate.

Two decisions there are worth knowing about, because both trade a little exposure for
a lot of correctness. `qti-assessment-stimulus-ref` is **kept**: strip it and the
candidate loses the reading passage the question is about. `qti-catalog-info` is
**kept**: it carries accessibility alternatives, and removing accommodations is a
worse failure than the marginal leak it would prevent. `qti-stylesheet`, by contrast,
is stripped — author CSS can single out the correct choice, and it would also have the
candidate's browser fetching a third-party URL mid-exam.

Redaction is one control in a layered scheme. The others are the caller's job: don't
register the renderer's response-processing components, accept only responses (never
outcomes) from the client, bind attempts server-side, and withhold scores until
release.

## Failing loudly

pyqti raises rather than ignoring QTI it does not understand. This is a deliberate
choice specific to assessment: a response-processing engine that silently ignores an
unresolvable template leaves every outcome at its declared default, and a redaction
pass that silently passes through an element it does not recognise may publish the
answer. Both mis-grade the candidate, and both look like success.

`examples/firstexample.xml` is a live example of why. Taken from the 1EdTech
Beginner's Guide, it declares `SCORE` with a `qti-default-value` of **1** and carries
no inline response processing at all --- only `template="...match_correct"`. An
engine that failed to resolve that URI, or that skipped the template's
`qti-response-else` branch, would score every wrong answer as 1.0.

## Notes on the implementation

Two aspects of the generated models shape the code more than anything else, and both
are documented in the modules that deal with them:

- **Element names, not Python classes** (`pyqti/qtitree.py`). QTI's expression
  operators are anonymous XSD types, so xsdata regenerated each one as a nested
  subclass per containing class --- `qti-match` is `ResponseIfDtype.QtiMatch`,
  `SetValueDtype.QtiMatch`, `LogicPairDtype.QtiMatch` and more. Dispatch therefore
  recovers the QTI element name from xsdata's field metadata. Similarly `base-type`
  and `cardinality` were each generated several times over, so `pyqti/values.py`
  normalises them and nothing compares the generated enums directly.
- **Mixed content has two incompatible shapes** (`pyqti/qtitree.py`). QTI containers
  are either block-only compound `Elements` fields or mixed `content: list[object]`
  wildcards, and tails are represented two different ways: usually as a separate
  string in the parent list, but absorbed *into* the element when that element's own
  model has a wildcard field. `prune()` handles the second case explicitly, because
  deleting such an element would otherwise silently swallow the rest of the sentence.

All contact with xsdata is confined to `pyqti/_xsdata.py` and `pyqti/qtitree.py`.
Several of the APIs used there are not part of xsdata's documented public surface,
which is why `pyproject.toml` pins `xsdata<27`; an earlier prototype in this repo
broke on exactly that (it called `XmlSerializer.next_value`, which no longer exists).
`tests/test_qtitree.py` asserts the structural assumptions so a model regeneration or
dependency bump fails fast and loudly.

Note also that xsdata does **not** validate against the schema.
`fail_on_converter_warnings` and `fail_on_unknown_properties` catch most authoring
mistakes, but real XSD validation would need lxml, which this project avoids (below).

## Auto-generated Models

**DO NOT MANUALLY EDIT THE MODELS IN pyqti.models!** The models were automatically generated using [`xsdata`](https://xsdata.readthedocs.io/en/latest/), specifically using the invocation:

`xsdata generate imsqti_asiv3p0_v1p0.xsd --structure-style namespace-clusters --package pyqti.models --compound-fields`

Note that this invocation predates the move to a `src/` layout, so it needs adjusting
so output lands in `src/pyqti/models` before the next regeneration. The
`--compound-fields` flag in particular is load-bearing: without it the generated field
names change wholesale and `pyqti/qtitree.py` stops working.

The source XSD file came from the [QTI 3.0 Specification Documents](https://www.1edtech.org/standards/qti/index#QTI3) section of 1EdTech's site, specifically the [zip file](https://www.imsglobal.org/sites/default/files/spec/qti/v3/xsdset/qtiv3p0_xsdsetv1p0.zip) containing all QTI 3.0 schemas.

I did look at [`xsdata-pydantic`](https://xsdata-pydantic.readthedocs.io/en/latest/), but the generated Pydantic models used a prohibitively large amount of memory during the parsing process for a small adaptive assessment item example (1.5 MB for the dataclasses version vs. 270 MB for the Pydantic models). My guess is that this is a memory leak bug somewhere rather than being something intrinsic to Pydantic, but I didn't want to try to track it down.

I also intentionally don't use the optional lxml bindings, because the speedups aren't worth the memory overhead (about 18 MB for that same example data).

The total memory usage for the auto-generated dataclass models is around 38 MB. This includes a lot of W3C related models that are referenced by the QTI spec and are necessary for full validation (e.g. MathML). If further memory optimization is necessary, we might be able to relax the parsing rules and model generation around these, though I don't think that's good tradeoff overall.

Because that budget matters, `pyqti/__init__.py` resolves its exports lazily: a bare
`import pyqti` does not pull in `pyqti.models`. Beware that `resource.ru_maxrss` is
kilobytes on Linux and bytes on macOS --- `pyqti/scripts/overhead.py` now scales for
both, so its figures no longer disagree by 1000x depending on the platform.
