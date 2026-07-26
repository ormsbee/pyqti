# Follow-up work

Known gaps, recorded so they are not rediscovered. Grouped by consequence rather than
by effort. Nothing here is planned or designed yet.

Provenance: most of the redaction items came out of an adversarial audit of the leak
surface after `b2b60e3`. Items marked **[verified]** were reproduced by running content
through `presentation_xml()`; items marked **[unverified]** are reasoned from the
generated models and the spec but have not been demonstrated.

---

## 1. Can defeat redaction outright

These bypass the redaction layer rather than slipping through it, so they matter more
than anything below.

- **Every `href` / `src` in the published XML is an unmediated second fetch.**
  `presentation_xml()` redacts the item document, but the browser then fetches
  whatever the document points at: `qti-assessment-stimulus-ref/@href`, `img/@src`,
  `object/@data`, `audio`/`video`/`track`, `xi:include/@href`, PCI `@module`. If any
  resolves to the authored file on disk or an unfiltered CDN path, redaction is
  bypassed completely. Either rewrite every URL to a pyqti-mediated route, or fail
  closed on any URL that does not already match one. **[unverified]** — no fixture
  currently carries an external reference.

- **`redact_stimulus()` does not exist.** `pyqti/redaction.py` keeps
  `qti_assessment_stimulus_ref` on the grounds that stripping it would remove the
  reading passage, and its docstring promises "the stimulus it names must itself be
  served through this same redaction path". There is no code behind that promise —
  `redact_for_delivery` is typed to `QtiAssessmentItem`, and `QtiAssessmentStimulus`
  has its own `qti-stylesheet` and `qti-catalog-info`. **[verified]** absent.

## 2. Publishes an item that is broken or misleading

- **`adaptive="true"` is published, but all feedback is stripped.** An adaptive item
  depends on feedback between attempts, so the candidate receives a broken item rather
  than a reduced one. Should raise until per-attempt feedback delivery exists.
  `KEEP` in `pyqti/redaction.py`. **[unverified]**

- **`show-hide` / `template-identifier` conditions are published with the template
  declarations cleared.** "Show this choice iff template variable X" with no X to
  evaluate is undefined behaviour, and the condition itself is answer-adjacent.
  `show-hide="hide"` also survives serialization (`show` is the XSD default and gets
  dropped, `hide` does not), so a hidden choice becomes a *marked* choice. Resolve
  server-side: evaluate the condition, drop hidden choices from the published XML, emit
  neither attribute. 14 classes carry `template-identifier`, 17 carry `show-hide`.
  **[unverified]**

- **Element order can be the answer.** If the bank convention is "key first", document
  order leaks it, and redaction cannot see that. The server-fixed shuffle order in §5
  would neutralise it. **[unverified, and unfalsifiable from content alone]**

- **`qti-companion-materials-info` is cleared wholesale.** `qti-calculator`,
  `qti-protractor` and `qti-rule` are legitimate tools a candidate may be entitled to;
  clearing the element removes them. Needs an allowlist rather than deletion, like
  `qti-catalog-info` already has.

## 3. Verification gaps

The current suite tests the four fixtures in `examples/`. That is coverage of the
corpus, not of the redaction.

- **A static allowlist over the model graph.** Compute the closure of
  `(element, attribute)` pairs *reachable* in a published document by walking `XmlVar`
  metadata from `QtiAssessmentItem`, minus everything redaction removes, and assert
  set equality against a frozen literal. This fails when the *model* gains a way to
  leak, before any fixture exists — which is the actual threat. Equality, not subset:
  a subset check passes silently when redaction gets too aggressive and starts eating
  candidate prose. `tests/test_qtitree.py` already has the precedent and `qtitree.py`
  has the machinery.

- **`ignore_default_attributes=True` silently omits *any* attribute equal to its XSD
  default, and only `max-choices` is pinned.** Every such attribute is a bet that
  Citolab's hand-written TypeScript defaults match the schema's — `max-choices` was
  checked and does, but `min-choices`, `shuffle`, `orientation` and `dir` were not, and
  `dir` matters for RTL. Pin the ones the front end actually reads.

  Measured rather than assumed: across the four fixtures the attributes present in
  source but absent from output are exactly `max-choices` and `default-value` (the
  latter on `qti-mapping`). That is narrower than it sounds — the fixtures simply do
  not set most defaults explicitly, so the real exposure is the set of *field* defaults
  in the generated models, not what these four items happen to contain. Assert against
  the model field defaults directly, or a new fixture will quietly change the answer.
  `tests/test_serialization.py`. **[verified]**

- **Pin what parse→serialize already gives us for free.** XML comments, processing
  instructions and DOCTYPE are all dropped, including an `<!-- ANSWER IS A -->` inline
  in a `<p>`. That is a real advantage over any textual redaction and deserves an
  explicit test so nobody "optimises" to string surgery later. Also assert
  `SerializerConfig.schema_location` stays `None`. **[verified]** as working, unpinned.

- **A property test** over fixtures × structural mutations: inject a foreign attribute
  at every node, a foreign element at every wildcard, flip every `view`/`use`/
  `show-hide` enum, assert no sentinel survives. A hand-rolled enumeration over
  `iter_children` is enough; no new dependency needed.

- **`test_authoritative_model_is_untouched` only checks `correct_value`.** A
  full-serialization equality check before and after redaction is strictly stronger and
  costs nothing. Note `ItemDefinition` is `frozen=True` but `ItemDefinition.model` is a
  mutable `QtiAssessmentItem`.

## 4. Fail-closed cases still missing

`pyqti/redaction.py` raises on an unclassified item field. It should also raise on:

- `qti-custom-interaction` and `qti-portable-custom-interaction` — `any_element` plus
  `other_attributes`, i.e. uninspectable by construction. PCI additionally carries
  `qti-interaction-markup` (full HTML, including feedback and printed variables) and
  `@module`, a JS URL. Neither is allowlisted today, so they fail the test
  incidentally; make it explicit.
- `xi:include` — `README.md` already lists XInclude as unimplemented; redaction should
  agree rather than silently dropping it.
- `qti-end-attempt-interaction` — a hint mechanism, and hints without server-side
  attempt state are a scoring hole. Reachable inside `<p>`. **[verified]** reachable.
  Note `ItemDefinition.from_model` validates undeclared response bindings only for
  choice interactions, so `response-identifier="HINT"` against no declaration passes
  silently.
- Any `any_attributes` / `other_attributes` still non-empty after `_scrub_attributes`,
  or any `AnyElement` surviving into the published tree — both indicate a bug in the
  walk rather than unsupported content.
- Any `href`/`src` that is not already a pyqti-mediated URL (see §1).

## 5. Delivery correctness required before real high-stakes use

Also summarised in `README.md`; repeated here because each is also a safety property.

- **Durable server-side session state and attempt binding.** `ItemSession` is in-memory
  per request. Nothing enforces `max-attempts`, and nothing ties a submission to an
  item the candidate was actually served.
- **Server-fixed shuffle order.** Citolab reads a `seed` from
  `qtiContext.QTI_CONTEXT.seed`, so pyqti should choose and record one per attempt.
  Honour `fixed` on individual choices. This is also the fix for the ordering leak in §2.
- **Template processing.** Run it server-side, then republish *only* the template
  variables referenced from the published body (`qti-printed-variable/@identifier`,
  `template-identifier`, `qti-template-inline`/`-block`, PCI `qti-template-variable`,
  MathML `<ci>`), with resolved defaults. Never republish a variable used only by
  response processing — `qti-set-correct-response` means the answer is computed at
  template time.
- **Withhold outcomes until score release.** The demo returns scores on submit, which
  is right for a demo and wrong for an exam: it hands back an oracle for probing.
  Score release should be a separate, policy-gated step.

## 6. Smaller items

- **`pyproject.toml` has no `license` field**, so the wheel metadata does not declare
  AGPL-3.0 even though `LICENSE` is present (`022249e`).
- **Browser verification of the Citolab render has never been done.** All presentation
  is client-side now, so no Python test can confirm the item displays. Needs
  `uv run qti-demo` plus network access for the CDN.
- **Open question: does Citolab need `qti-response-declaration` at all?** Its
  interactions read `response-identifier` off the interaction element. If declarations
  are unnecessary, dropping them removes a whole tier of published surface. Answerable
  with one browser test.
- **`match-group` / `match-max` / `match-min`** on `GapTextDtype`,
  `SimpleAssociableChoiceDtype`, `GapImgDtype` are presentation-required and cannot be
  deleted, but `match-group` narrowed to a single target *is* the answer, and
  `match-max="0"` on distractors is a classic tell. Belongs in an authoring lint rather
  than in redaction. Only relevant once match/gap-match interactions are supported.
- **`qti-catalog-info` cards are published regardless of the candidate's PNP.** The
  candidate needs only the cards their profile entitles them to. Filtering by an
  allowlist of honoured `support` values is the eventual shape; unlike everything else
  in §4, an unsupported support type should be dropped silently rather than raised on —
  it is normal content, not an error.
