# PyQTI

An early implementation of the QTI 3.0 standard for Python.

The first goal is going to be to get simple multiple choice problems to render.

## Auto-generated Models

**DO NOT MANUALLY EDIT THE MODELS IN pyqti.models!** The models were automatically generated using [`xsdata`](https://xsdata.readthedocs.io/en/latest/), specifically using the invocation:

`xsdata imsqti_asiv3p0_v1p0.xsd --structure-style namespace-clusters --package pyqti.models --compound-fields`

The source XSD file came from the [QTI 3.0 Specification Documents](https://www.1edtech.org/standards/qti/index#QTI3) section of 1EdTech's site, specifically the [zip file](https://www.imsglobal.org/sites/default/files/spec/qti/v3/xsdset/qtiv3p0_xsdsetv1p0.zip) containing all QTI 3.0 schemas.

I did look at [`xsdata-pydantic`](https://xsdata-pydantic.readthedocs.io/en/latest/), but the generated Pydantic models used a prohibitively large amount of memory during the parsing process for a small adaptive assessment item example (1.5 MB for the dataclasses version vs. 270 MB for the Pydantic models). My guess is that this is a memory leak bug somewhere rather than being something intrinsic to Pydantic, but I didn't want to try to track it down.

We also intentionally don't use the optional lxml bindings, because the speedups aren't worth the memory overhead (about 18 MB for that same example data).

The total memory usage for the auto-generated dataclass models is around 38 MB. This includes a lot of W3C related models that are referenced by the QTI spec and are necessary for full validation (e.g. MathML).
