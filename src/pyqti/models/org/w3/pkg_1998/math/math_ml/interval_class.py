from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from pyqti.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from pyqti.models.org.w3.pkg_1998.math.math_ml.approx import Approx
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccos import Arccos
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccosh import Arccosh
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccot import Arccot
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccoth import Arccoth
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccsc import Arccsc
from pyqti.models.org.w3.pkg_1998.math.math_ml.arccsch import Arccsch
from pyqti.models.org.w3.pkg_1998.math.math_ml.arcsec import Arcsec
from pyqti.models.org.w3.pkg_1998.math.math_ml.arcsech import Arcsech
from pyqti.models.org.w3.pkg_1998.math.math_ml.arcsin import Arcsin
from pyqti.models.org.w3.pkg_1998.math.math_ml.arcsinh import Arcsinh
from pyqti.models.org.w3.pkg_1998.math.math_ml.arctan import Arctan
from pyqti.models.org.w3.pkg_1998.math.math_ml.arctanh import Arctanh
from pyqti.models.org.w3.pkg_1998.math.math_ml.arg import Arg
from pyqti.models.org.w3.pkg_1998.math.math_ml.card import Card
from pyqti.models.org.w3.pkg_1998.math.math_ml.cartesianproduct import (
    Cartesianproduct,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.cbytes import Cbytes
from pyqti.models.org.w3.pkg_1998.math.math_ml.ceiling import Ceiling
from pyqti.models.org.w3.pkg_1998.math.math_ml.cerror import (
    Apply,
    Bind,
    Cerror,
    Ci,
    Cn,
    Csymbol,
    Declare,
    Fn,
    List,
    Piecewise,
    Reln,
    Set,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from pyqti.models.org.w3.pkg_1998.math.math_ml.complexes import Complexes
from pyqti.models.org.w3.pkg_1998.math.math_ml.compose import Compose
from pyqti.models.org.w3.pkg_1998.math.math_ml.conjugate import Conjugate
from pyqti.models.org.w3.pkg_1998.math.math_ml.cos import Cos
from pyqti.models.org.w3.pkg_1998.math.math_ml.cosh import Cosh
from pyqti.models.org.w3.pkg_1998.math.math_ml.cot import Cot
from pyqti.models.org.w3.pkg_1998.math.math_ml.coth import Coth
from pyqti.models.org.w3.pkg_1998.math.math_ml.cs import Cs
from pyqti.models.org.w3.pkg_1998.math.math_ml.csc import Csc
from pyqti.models.org.w3.pkg_1998.math.math_ml.csch import Csch
from pyqti.models.org.w3.pkg_1998.math.math_ml.curl import Curl
from pyqti.models.org.w3.pkg_1998.math.math_ml.determinant import Determinant
from pyqti.models.org.w3.pkg_1998.math.math_ml.diff import Diff
from pyqti.models.org.w3.pkg_1998.math.math_ml.divergence import Divergence
from pyqti.models.org.w3.pkg_1998.math.math_ml.divide import Divide
from pyqti.models.org.w3.pkg_1998.math.math_ml.domain import Domain
from pyqti.models.org.w3.pkg_1998.math.math_ml.emptyset import Emptyset
from pyqti.models.org.w3.pkg_1998.math.math_ml.eq import Eq
from pyqti.models.org.w3.pkg_1998.math.math_ml.equivalent import Equivalent
from pyqti.models.org.w3.pkg_1998.math.math_ml.eulergamma import Eulergamma
from pyqti.models.org.w3.pkg_1998.math.math_ml.exists import Exists
from pyqti.models.org.w3.pkg_1998.math.math_ml.exp import Exp
from pyqti.models.org.w3.pkg_1998.math.math_ml.exponentiale import Exponentiale
from pyqti.models.org.w3.pkg_1998.math.math_ml.factorial import Factorial
from pyqti.models.org.w3.pkg_1998.math.math_ml.factorof import Factorof
from pyqti.models.org.w3.pkg_1998.math.math_ml.false import FalseType
from pyqti.models.org.w3.pkg_1998.math.math_ml.floor import Floor
from pyqti.models.org.w3.pkg_1998.math.math_ml.forall import Forall
from pyqti.models.org.w3.pkg_1998.math.math_ml.gcd import Gcd
from pyqti.models.org.w3.pkg_1998.math.math_ml.geq import Geq
from pyqti.models.org.w3.pkg_1998.math.math_ml.grad import Grad
from pyqti.models.org.w3.pkg_1998.math.math_ml.gt import Gt
from pyqti.models.org.w3.pkg_1998.math.math_ml.ident import Ident
from pyqti.models.org.w3.pkg_1998.math.math_ml.image import Image
from pyqti.models.org.w3.pkg_1998.math.math_ml.imaginary import Imaginary
from pyqti.models.org.w3.pkg_1998.math.math_ml.imaginaryi import Imaginaryi
from pyqti.models.org.w3.pkg_1998.math.math_ml.implies import Implies
from pyqti.models.org.w3.pkg_1998.math.math_ml.in_mod import In
from pyqti.models.org.w3.pkg_1998.math.math_ml.infinity import Infinity
from pyqti.models.org.w3.pkg_1998.math.math_ml.int_mod import Int
from pyqti.models.org.w3.pkg_1998.math.math_ml.integers import Integers
from pyqti.models.org.w3.pkg_1998.math.math_ml.intersect import Intersect
from pyqti.models.org.w3.pkg_1998.math.math_ml.interval import Interval
from pyqti.models.org.w3.pkg_1998.math.math_ml.inverse import Inverse
from pyqti.models.org.w3.pkg_1998.math.math_ml.lambda_mod import Lambda
from pyqti.models.org.w3.pkg_1998.math.math_ml.laplacian import Laplacian
from pyqti.models.org.w3.pkg_1998.math.math_ml.lcm import Lcm
from pyqti.models.org.w3.pkg_1998.math.math_ml.leq import Leq
from pyqti.models.org.w3.pkg_1998.math.math_ml.limit import Limit
from pyqti.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from pyqti.models.org.w3.pkg_1998.math.math_ml.log import Log
from pyqti.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from pyqti.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from pyqti.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from pyqti.models.org.w3.pkg_1998.math.math_ml.max import Max
from pyqti.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from pyqti.models.org.w3.pkg_1998.math.math_ml.median import Median
from pyqti.models.org.w3.pkg_1998.math.math_ml.min import Min
from pyqti.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from pyqti.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from pyqti.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from pyqti.models.org.w3.pkg_1998.math.math_ml.naturalnumbers import (
    Naturalnumbers,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.neq import Neq
from pyqti.models.org.w3.pkg_1998.math.math_ml.not_mod import Not
from pyqti.models.org.w3.pkg_1998.math.math_ml.notanumber import Notanumber
from pyqti.models.org.w3.pkg_1998.math.math_ml.notin import Notin
from pyqti.models.org.w3.pkg_1998.math.math_ml.notprsubset import Notprsubset
from pyqti.models.org.w3.pkg_1998.math.math_ml.notsubset import Notsubset
from pyqti.models.org.w3.pkg_1998.math.math_ml.or_mod import Or
from pyqti.models.org.w3.pkg_1998.math.math_ml.outerproduct import Outerproduct
from pyqti.models.org.w3.pkg_1998.math.math_ml.partialdiff import Partialdiff
from pyqti.models.org.w3.pkg_1998.math.math_ml.pi import Pi
from pyqti.models.org.w3.pkg_1998.math.math_ml.plus import Plus
from pyqti.models.org.w3.pkg_1998.math.math_ml.power import Power
from pyqti.models.org.w3.pkg_1998.math.math_ml.primes import Primes
from pyqti.models.org.w3.pkg_1998.math.math_ml.product import Product
from pyqti.models.org.w3.pkg_1998.math.math_ml.prsubset import Prsubset
from pyqti.models.org.w3.pkg_1998.math.math_ml.quotient import Quotient
from pyqti.models.org.w3.pkg_1998.math.math_ml.rationals import Rationals
from pyqti.models.org.w3.pkg_1998.math.math_ml.real import Real
from pyqti.models.org.w3.pkg_1998.math.math_ml.reals import Reals
from pyqti.models.org.w3.pkg_1998.math.math_ml.rem import Rem
from pyqti.models.org.w3.pkg_1998.math.math_ml.root import Root
from pyqti.models.org.w3.pkg_1998.math.math_ml.scalarproduct import (
    Scalarproduct,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.sdev import Sdev
from pyqti.models.org.w3.pkg_1998.math.math_ml.sec import Sec
from pyqti.models.org.w3.pkg_1998.math.math_ml.sech import Sech
from pyqti.models.org.w3.pkg_1998.math.math_ml.selector import Selector
from pyqti.models.org.w3.pkg_1998.math.math_ml.setdiff import Setdiff
from pyqti.models.org.w3.pkg_1998.math.math_ml.share import Share
from pyqti.models.org.w3.pkg_1998.math.math_ml.sin import Sin
from pyqti.models.org.w3.pkg_1998.math.math_ml.sinh import Sinh
from pyqti.models.org.w3.pkg_1998.math.math_ml.subset import Subset
from pyqti.models.org.w3.pkg_1998.math.math_ml.sum import Sum
from pyqti.models.org.w3.pkg_1998.math.math_ml.tan import Tan
from pyqti.models.org.w3.pkg_1998.math.math_ml.tanh import Tanh
from pyqti.models.org.w3.pkg_1998.math.math_ml.tendsto import Tendsto
from pyqti.models.org.w3.pkg_1998.math.math_ml.times import Times
from pyqti.models.org.w3.pkg_1998.math.math_ml.transpose import Transpose
from pyqti.models.org.w3.pkg_1998.math.math_ml.true import TrueType
from pyqti.models.org.w3.pkg_1998.math.math_ml.union import UnionType
from pyqti.models.org.w3.pkg_1998.math.math_ml.variance import Variance
from pyqti.models.org.w3.pkg_1998.math.math_ml.vector import Vector
from pyqti.models.org.w3.pkg_1998.math.math_ml.vectorproduct import (
    Vectorproduct,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass(kw_only=True)
class IntervalClass:
    class Meta:
        name = "interval.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    apply: list[Apply] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    bind: list[Bind] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    ci: list[Ci] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    cn: list[Cn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    csymbol: list[Csymbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    cbytes: list[Cbytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    cerror: list[Cerror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    cs: list[Cs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    share: list[Share] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    piecewise: list[Piecewise] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    declare_or_fn_or_reln: list[Declare | Fn | Reln] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "declare",
                    "type": Declare,
                    "max_occurs": 2,
                },
                {
                    "name": "fn",
                    "type": Fn,
                    "max_occurs": 2,
                },
                {
                    "name": "reln",
                    "type": Reln,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    interval: list[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    choice: list[
        Moment | Log | Ln | Image | Codomain | Domain | Ident | Inverse
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "moment",
                    "type": Moment,
                    "max_occurs": 2,
                },
                {
                    "name": "log",
                    "type": Log,
                    "max_occurs": 2,
                },
                {
                    "name": "ln",
                    "type": Ln,
                    "max_occurs": 2,
                },
                {
                    "name": "image",
                    "type": Image,
                    "max_occurs": 2,
                },
                {
                    "name": "codomain",
                    "type": Codomain,
                    "max_occurs": 2,
                },
                {
                    "name": "domain",
                    "type": Domain,
                    "max_occurs": 2,
                },
                {
                    "name": "ident",
                    "type": Ident,
                    "max_occurs": 2,
                },
                {
                    "name": "inverse",
                    "type": Inverse,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    lambda_value: list[Lambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    compose: list[Compose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    quotient: list[Quotient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    divide: list[Divide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    minus: list[Minus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    power: list[Power] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    rem: list[Rem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    root: list[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    factorial: list[Factorial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    abs: list[Abs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    conjugate: list[Conjugate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    arg: list[Arg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    real: list[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    imaginary: list[Imaginary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    floor: list[Floor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    ceiling: list[Ceiling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    exp: list[Exp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    min_or_max: list[Min | Max] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "min",
                    "type": Min,
                    "max_occurs": 2,
                },
                {
                    "name": "max",
                    "type": Max,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_1: list[Lcm | Gcd | Times | Plus] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "lcm",
                    "type": Lcm,
                    "max_occurs": 2,
                },
                {
                    "name": "gcd",
                    "type": Gcd,
                    "max_occurs": 2,
                },
                {
                    "name": "times",
                    "type": Times,
                    "max_occurs": 2,
                },
                {
                    "name": "plus",
                    "type": Plus,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    xor_or_or_or_and: list[Xor | Or | And] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "xor",
                    "type": Xor,
                    "max_occurs": 2,
                },
                {
                    "name": "or",
                    "type": Or,
                    "max_occurs": 2,
                },
                {
                    "name": "and",
                    "type": And,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    not_value: list[Not] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    equivalent_or_implies: list[Equivalent | Implies] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "equivalent",
                    "type": Equivalent,
                    "max_occurs": 2,
                },
                {
                    "name": "implies",
                    "type": Implies,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    exists_or_forall: list[Exists | Forall] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "exists",
                    "type": Exists,
                    "max_occurs": 2,
                },
                {
                    "name": "forall",
                    "type": Forall,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_2: list[Leq | Geq | Lt | Gt | Eq] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "leq",
                    "type": Leq,
                    "max_occurs": 2,
                },
                {
                    "name": "geq",
                    "type": Geq,
                    "max_occurs": 2,
                },
                {
                    "name": "lt",
                    "type": Lt,
                    "max_occurs": 2,
                },
                {
                    "name": "gt",
                    "type": Gt,
                    "max_occurs": 2,
                },
                {
                    "name": "eq",
                    "type": Eq,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_3: list[Tendsto | Factorof | Approx | Neq] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "tendsto",
                    "type": Tendsto,
                    "max_occurs": 2,
                },
                {
                    "name": "factorof",
                    "type": Factorof,
                    "max_occurs": 2,
                },
                {
                    "name": "approx",
                    "type": Approx,
                    "max_occurs": 2,
                },
                {
                    "name": "neq",
                    "type": Neq,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    int_value: list[Int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    diff: list[Diff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    partialdiff: list[Partialdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    choice_4: list[Laplacian | Curl | Grad | Divergence] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "laplacian",
                    "type": Laplacian,
                    "max_occurs": 2,
                },
                {
                    "name": "curl",
                    "type": Curl,
                    "max_occurs": 2,
                },
                {
                    "name": "grad",
                    "type": Grad,
                    "max_occurs": 2,
                },
                {
                    "name": "divergence",
                    "type": Divergence,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    list_or_set: list[List | Set] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "list",
                    "type": List,
                    "max_occurs": 2,
                },
                {
                    "name": "set",
                    "type": Set,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    cartesianproduct_or_intersect_or_union: list[
        Cartesianproduct | Intersect | UnionType
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "cartesianproduct",
                    "type": Cartesianproduct,
                    "max_occurs": 2,
                },
                {
                    "name": "intersect",
                    "type": Intersect,
                    "max_occurs": 2,
                },
                {
                    "name": "union",
                    "type": UnionType,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_5: list[Setdiff | Notprsubset | Notsubset | Notin | In] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "setdiff",
                    "type": Setdiff,
                    "max_occurs": 2,
                },
                {
                    "name": "notprsubset",
                    "type": Notprsubset,
                    "max_occurs": 2,
                },
                {
                    "name": "notsubset",
                    "type": Notsubset,
                    "max_occurs": 2,
                },
                {
                    "name": "notin",
                    "type": Notin,
                    "max_occurs": 2,
                },
                {
                    "name": "in",
                    "type": In,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    prsubset_or_subset: list[Prsubset | Subset] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "prsubset",
                    "type": Prsubset,
                    "max_occurs": 2,
                },
                {
                    "name": "subset",
                    "type": Subset,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    card: list[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    sum: list[Sum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    product: list[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    limit: list[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    choice_6: list[
        Arctanh
        | Arcsinh
        | Arcsech
        | Arcsec
        | Arccsch
        | Arccsc
        | Arccoth
        | Arccot
        | Arccosh
        | Arctan
        | Arccos
        | Arcsin
        | Coth
        | Csch
        | Sech
        | Tanh
        | Cosh
        | Sinh
        | Cot
        | Csc
        | Sec
        | Tan
        | Cos
        | Sin
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "arctanh",
                    "type": Arctanh,
                    "max_occurs": 2,
                },
                {
                    "name": "arcsinh",
                    "type": Arcsinh,
                    "max_occurs": 2,
                },
                {
                    "name": "arcsech",
                    "type": Arcsech,
                    "max_occurs": 2,
                },
                {
                    "name": "arcsec",
                    "type": Arcsec,
                    "max_occurs": 2,
                },
                {
                    "name": "arccsch",
                    "type": Arccsch,
                    "max_occurs": 2,
                },
                {
                    "name": "arccsc",
                    "type": Arccsc,
                    "max_occurs": 2,
                },
                {
                    "name": "arccoth",
                    "type": Arccoth,
                    "max_occurs": 2,
                },
                {
                    "name": "arccot",
                    "type": Arccot,
                    "max_occurs": 2,
                },
                {
                    "name": "arccosh",
                    "type": Arccosh,
                    "max_occurs": 2,
                },
                {
                    "name": "arctan",
                    "type": Arctan,
                    "max_occurs": 2,
                },
                {
                    "name": "arccos",
                    "type": Arccos,
                    "max_occurs": 2,
                },
                {
                    "name": "arcsin",
                    "type": Arcsin,
                    "max_occurs": 2,
                },
                {
                    "name": "coth",
                    "type": Coth,
                    "max_occurs": 2,
                },
                {
                    "name": "csch",
                    "type": Csch,
                    "max_occurs": 2,
                },
                {
                    "name": "sech",
                    "type": Sech,
                    "max_occurs": 2,
                },
                {
                    "name": "tanh",
                    "type": Tanh,
                    "max_occurs": 2,
                },
                {
                    "name": "cosh",
                    "type": Cosh,
                    "max_occurs": 2,
                },
                {
                    "name": "sinh",
                    "type": Sinh,
                    "max_occurs": 2,
                },
                {
                    "name": "cot",
                    "type": Cot,
                    "max_occurs": 2,
                },
                {
                    "name": "csc",
                    "type": Csc,
                    "max_occurs": 2,
                },
                {
                    "name": "sec",
                    "type": Sec,
                    "max_occurs": 2,
                },
                {
                    "name": "tan",
                    "type": Tan,
                    "max_occurs": 2,
                },
                {
                    "name": "cos",
                    "type": Cos,
                    "max_occurs": 2,
                },
                {
                    "name": "sin",
                    "type": Sin,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_7: list[Mode | Median | Variance | Sdev | Mean] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "mode",
                    "type": Mode,
                    "max_occurs": 2,
                },
                {
                    "name": "median",
                    "type": Median,
                    "max_occurs": 2,
                },
                {
                    "name": "variance",
                    "type": Variance,
                    "max_occurs": 2,
                },
                {
                    "name": "sdev",
                    "type": Sdev,
                    "max_occurs": 2,
                },
                {
                    "name": "mean",
                    "type": Mean,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    matrixrow_or_matrix_or_vector: list[Matrixrow | Matrix | Vector] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "matrixrow",
                    "type": Matrixrow,
                    "max_occurs": 2,
                },
                {
                    "name": "matrix",
                    "type": Matrix,
                    "max_occurs": 2,
                },
                {
                    "name": "vector",
                    "type": Vector,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    transpose_or_determinant: list[Transpose | Determinant] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "transpose",
                    "type": Transpose,
                    "max_occurs": 2,
                },
                {
                    "name": "determinant",
                    "type": Determinant,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    selector: list[Selector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    outerproduct_or_scalarproduct_or_vectorproduct: list[
        Outerproduct | Scalarproduct | Vectorproduct
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "outerproduct",
                    "type": Outerproduct,
                    "max_occurs": 2,
                },
                {
                    "name": "scalarproduct",
                    "type": Scalarproduct,
                    "max_occurs": 2,
                },
                {
                    "name": "vectorproduct",
                    "type": Vectorproduct,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_8: list[
        Emptyset
        | Primes
        | Complexes
        | Naturalnumbers
        | Rationals
        | Reals
        | Integers
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "emptyset",
                    "type": Emptyset,
                    "max_occurs": 2,
                },
                {
                    "name": "primes",
                    "type": Primes,
                    "max_occurs": 2,
                },
                {
                    "name": "complexes",
                    "type": Complexes,
                    "max_occurs": 2,
                },
                {
                    "name": "naturalnumbers",
                    "type": Naturalnumbers,
                    "max_occurs": 2,
                },
                {
                    "name": "rationals",
                    "type": Rationals,
                    "max_occurs": 2,
                },
                {
                    "name": "reals",
                    "type": Reals,
                    "max_occurs": 2,
                },
                {
                    "name": "integers",
                    "type": Integers,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    choice_9: list[
        Infinity
        | Eulergamma
        | Pi
        | FalseType
        | TrueType
        | Notanumber
        | Imaginaryi
        | Exponentiale
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "infinity",
                    "type": Infinity,
                    "max_occurs": 2,
                },
                {
                    "name": "eulergamma",
                    "type": Eulergamma,
                    "max_occurs": 2,
                },
                {
                    "name": "pi",
                    "type": Pi,
                    "max_occurs": 2,
                },
                {
                    "name": "false",
                    "type": FalseType,
                    "max_occurs": 2,
                },
                {
                    "name": "true",
                    "type": TrueType,
                    "max_occurs": 2,
                },
                {
                    "name": "notanumber",
                    "type": Notanumber,
                    "max_occurs": 2,
                },
                {
                    "name": "imaginaryi",
                    "type": Imaginaryi,
                    "max_occurs": 2,
                },
                {
                    "name": "exponentiale",
                    "type": Exponentiale,
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: None | str = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
    closure: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
