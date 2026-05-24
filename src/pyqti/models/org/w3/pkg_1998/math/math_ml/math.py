from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

from pyqti.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from pyqti.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from pyqti.models.org.w3.pkg_1998.math.math_ml.annotation import Annotation
from pyqti.models.org.w3.pkg_1998.math.math_ml.annotation_xml import (
    AnnotationXml,
)
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
    Maction,
    Menclose,
    Merror,
    Mfenced,
    Mfrac,
    Mlongdiv,
    Mmultiscripts,
    Mover,
    Mpadded,
    Mphantom,
    Mroot,
    Mrow,
    Msqrt,
    Mstack,
    Mstyle,
    Msub,
    Msubsup,
    Msup,
    Munder,
    Munderover,
    Piecewise,
    Reln,
    Set,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from pyqti.models.org.w3.pkg_1998.math.math_ml.columnalignstyle import (
    Columnalignstyle,
)
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
from pyqti.models.org.w3.pkg_1998.math.math_ml.linestyle import Linestyle
from pyqti.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from pyqti.models.org.w3.pkg_1998.math.math_ml.log import Log
from pyqti.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from pyqti.models.org.w3.pkg_1998.math.math_ml.maligngroup import Maligngroup
from pyqti.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_accent import MathAccent
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_accentunder import (
    MathAccentunder,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_align import MathAlign
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_bevelled import (
    MathBevelled,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_charalign import (
    MathCharalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_denomalign import (
    MathDenomalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_dir import MathDir
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_display import MathDisplay
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_displaystyle import (
    MathDisplaystyle,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_edge import MathEdge
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_equalcolumns import (
    MathEqualcolumns,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_equalrows import (
    MathEqualrows,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_fence import MathFence
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_form import MathForm
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_indentalign import (
    MathIndentalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_indentalignfirst import (
    MathIndentalignfirst,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_indentalignlast import (
    MathIndentalignlast,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_infixlinebreakstyle import (
    MathInfixlinebreakstyle,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_largeop import MathLargeop
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_linebreak import (
    MathLinebreak,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_linebreakstyle import (
    MathLinebreakstyle,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_location import (
    MathLocation,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_longdivstyle import (
    MathLongdivstyle,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_mathvariant import (
    MathMathvariant,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_movablelimits import (
    MathMovablelimits,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_numalign import (
    MathNumalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_overflow import (
    MathOverflow,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_separator import (
    MathSeparator,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_side import MathSide
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_stackalign import (
    MathStackalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_stretchy import (
    MathStretchy,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_symmetric import (
    MathSymmetric,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math_value import MathValue
from pyqti.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from pyqti.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from pyqti.models.org.w3.pkg_1998.math.math_ml.max import Max
from pyqti.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from pyqti.models.org.w3.pkg_1998.math.math_ml.median import Median
from pyqti.models.org.w3.pkg_1998.math.math_ml.mi import Mi
from pyqti.models.org.w3.pkg_1998.math.math_ml.min import Min
from pyqti.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from pyqti.models.org.w3.pkg_1998.math.math_ml.mn import Mn
from pyqti.models.org.w3.pkg_1998.math.math_ml.mo import Mo
from pyqti.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from pyqti.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from pyqti.models.org.w3.pkg_1998.math.math_ml.ms import Ms
from pyqti.models.org.w3.pkg_1998.math.math_ml.mspace import Mspace
from pyqti.models.org.w3.pkg_1998.math.math_ml.mtable import Mtable
from pyqti.models.org.w3.pkg_1998.math.math_ml.mtext import Mtext
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
from pyqti.models.org.w3.pkg_1998.math.math_ml.verticalalign import (
    Verticalalign,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass(kw_only=True)
class Math:
    class Meta:
        name = "math"
        namespace = "http://www.w3.org/1998/Math/MathML"

    choice: list[
        Apply
        | Bind
        | Ci
        | Cn
        | Csymbol
        | Cbytes
        | Cerror
        | Cs
        | Share
        | Piecewise
        | Declare
        | Fn
        | Reln
        | Interval
        | Moment
        | Log
        | Ln
        | Image
        | Codomain
        | Domain
        | Ident
        | Inverse
        | Lambda
        | Compose
        | Quotient
        | Divide
        | Minus
        | Power
        | Rem
        | Root
        | Factorial
        | Abs
        | Conjugate
        | Arg
        | Real
        | Imaginary
        | Floor
        | Ceiling
        | Exp
        | Min
        | Max
        | Lcm
        | Gcd
        | Times
        | Plus
        | Xor
        | Or
        | And
        | Not
        | Equivalent
        | Implies
        | Exists
        | Forall
        | Leq
        | Geq
        | Lt
        | Gt
        | Eq
        | Tendsto
        | Factorof
        | Approx
        | Neq
        | Int
        | Diff
        | Partialdiff
        | Laplacian
        | Curl
        | Grad
        | Divergence
        | List
        | Set
        | Cartesianproduct
        | Intersect
        | UnionType
        | Setdiff
        | Notprsubset
        | Notsubset
        | Notin
        | In
        | Prsubset
        | Subset
        | Card
        | Sum
        | Product
        | Limit
        | Arctanh
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
        | Mode
        | Median
        | Variance
        | Sdev
        | Mean
        | Matrixrow
        | Matrix
        | Vector
        | Transpose
        | Determinant
        | Selector
        | Outerproduct
        | Scalarproduct
        | Vectorproduct
        | Emptyset
        | Primes
        | Complexes
        | Naturalnumbers
        | Rationals
        | Reals
        | Integers
        | Infinity
        | Eulergamma
        | Pi
        | FalseType
        | TrueType
        | Notanumber
        | Imaginaryi
        | Exponentiale
        | Maction
        | Mlongdiv
        | Mstack
        | Mtable
        | Mmultiscripts
        | Munderover
        | Mover
        | Munder
        | Msubsup
        | Msup
        | Msub
        | Menclose
        | Mfenced
        | Mphantom
        | Mpadded
        | Merror
        | Mstyle
        | Mroot
        | Msqrt
        | Mfrac
        | Mrow
        | Maligngroup
        | Malignmark
        | Ms
        | Mspace
        | Mtext
        | Mo
        | Mn
        | Mi
        | Math.Semantics
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "apply",
                    "type": Apply,
                },
                {
                    "name": "bind",
                    "type": Bind,
                },
                {
                    "name": "ci",
                    "type": Ci,
                },
                {
                    "name": "cn",
                    "type": Cn,
                },
                {
                    "name": "csymbol",
                    "type": Csymbol,
                },
                {
                    "name": "cbytes",
                    "type": Cbytes,
                },
                {
                    "name": "cerror",
                    "type": Cerror,
                },
                {
                    "name": "cs",
                    "type": Cs,
                },
                {
                    "name": "share",
                    "type": Share,
                },
                {
                    "name": "piecewise",
                    "type": Piecewise,
                },
                {
                    "name": "declare",
                    "type": Declare,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "reln",
                    "type": Reln,
                },
                {
                    "name": "interval",
                    "type": Interval,
                },
                {
                    "name": "moment",
                    "type": Moment,
                },
                {
                    "name": "log",
                    "type": Log,
                },
                {
                    "name": "ln",
                    "type": Ln,
                },
                {
                    "name": "image",
                    "type": Image,
                },
                {
                    "name": "codomain",
                    "type": Codomain,
                },
                {
                    "name": "domain",
                    "type": Domain,
                },
                {
                    "name": "ident",
                    "type": Ident,
                },
                {
                    "name": "inverse",
                    "type": Inverse,
                },
                {
                    "name": "lambda",
                    "type": Lambda,
                },
                {
                    "name": "compose",
                    "type": Compose,
                },
                {
                    "name": "quotient",
                    "type": Quotient,
                },
                {
                    "name": "divide",
                    "type": Divide,
                },
                {
                    "name": "minus",
                    "type": Minus,
                },
                {
                    "name": "power",
                    "type": Power,
                },
                {
                    "name": "rem",
                    "type": Rem,
                },
                {
                    "name": "root",
                    "type": Root,
                },
                {
                    "name": "factorial",
                    "type": Factorial,
                },
                {
                    "name": "abs",
                    "type": Abs,
                },
                {
                    "name": "conjugate",
                    "type": Conjugate,
                },
                {
                    "name": "arg",
                    "type": Arg,
                },
                {
                    "name": "real",
                    "type": Real,
                },
                {
                    "name": "imaginary",
                    "type": Imaginary,
                },
                {
                    "name": "floor",
                    "type": Floor,
                },
                {
                    "name": "ceiling",
                    "type": Ceiling,
                },
                {
                    "name": "exp",
                    "type": Exp,
                },
                {
                    "name": "min",
                    "type": Min,
                },
                {
                    "name": "max",
                    "type": Max,
                },
                {
                    "name": "lcm",
                    "type": Lcm,
                },
                {
                    "name": "gcd",
                    "type": Gcd,
                },
                {
                    "name": "times",
                    "type": Times,
                },
                {
                    "name": "plus",
                    "type": Plus,
                },
                {
                    "name": "xor",
                    "type": Xor,
                },
                {
                    "name": "or",
                    "type": Or,
                },
                {
                    "name": "and",
                    "type": And,
                },
                {
                    "name": "not",
                    "type": Not,
                },
                {
                    "name": "equivalent",
                    "type": Equivalent,
                },
                {
                    "name": "implies",
                    "type": Implies,
                },
                {
                    "name": "exists",
                    "type": Exists,
                },
                {
                    "name": "forall",
                    "type": Forall,
                },
                {
                    "name": "leq",
                    "type": Leq,
                },
                {
                    "name": "geq",
                    "type": Geq,
                },
                {
                    "name": "lt",
                    "type": Lt,
                },
                {
                    "name": "gt",
                    "type": Gt,
                },
                {
                    "name": "eq",
                    "type": Eq,
                },
                {
                    "name": "tendsto",
                    "type": Tendsto,
                },
                {
                    "name": "factorof",
                    "type": Factorof,
                },
                {
                    "name": "approx",
                    "type": Approx,
                },
                {
                    "name": "neq",
                    "type": Neq,
                },
                {
                    "name": "int",
                    "type": Int,
                },
                {
                    "name": "diff",
                    "type": Diff,
                },
                {
                    "name": "partialdiff",
                    "type": Partialdiff,
                },
                {
                    "name": "laplacian",
                    "type": Laplacian,
                },
                {
                    "name": "curl",
                    "type": Curl,
                },
                {
                    "name": "grad",
                    "type": Grad,
                },
                {
                    "name": "divergence",
                    "type": Divergence,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "set",
                    "type": Set,
                },
                {
                    "name": "cartesianproduct",
                    "type": Cartesianproduct,
                },
                {
                    "name": "intersect",
                    "type": Intersect,
                },
                {
                    "name": "union",
                    "type": UnionType,
                },
                {
                    "name": "setdiff",
                    "type": Setdiff,
                },
                {
                    "name": "notprsubset",
                    "type": Notprsubset,
                },
                {
                    "name": "notsubset",
                    "type": Notsubset,
                },
                {
                    "name": "notin",
                    "type": Notin,
                },
                {
                    "name": "in",
                    "type": In,
                },
                {
                    "name": "prsubset",
                    "type": Prsubset,
                },
                {
                    "name": "subset",
                    "type": Subset,
                },
                {
                    "name": "card",
                    "type": Card,
                },
                {
                    "name": "sum",
                    "type": Sum,
                },
                {
                    "name": "product",
                    "type": Product,
                },
                {
                    "name": "limit",
                    "type": Limit,
                },
                {
                    "name": "arctanh",
                    "type": Arctanh,
                },
                {
                    "name": "arcsinh",
                    "type": Arcsinh,
                },
                {
                    "name": "arcsech",
                    "type": Arcsech,
                },
                {
                    "name": "arcsec",
                    "type": Arcsec,
                },
                {
                    "name": "arccsch",
                    "type": Arccsch,
                },
                {
                    "name": "arccsc",
                    "type": Arccsc,
                },
                {
                    "name": "arccoth",
                    "type": Arccoth,
                },
                {
                    "name": "arccot",
                    "type": Arccot,
                },
                {
                    "name": "arccosh",
                    "type": Arccosh,
                },
                {
                    "name": "arctan",
                    "type": Arctan,
                },
                {
                    "name": "arccos",
                    "type": Arccos,
                },
                {
                    "name": "arcsin",
                    "type": Arcsin,
                },
                {
                    "name": "coth",
                    "type": Coth,
                },
                {
                    "name": "csch",
                    "type": Csch,
                },
                {
                    "name": "sech",
                    "type": Sech,
                },
                {
                    "name": "tanh",
                    "type": Tanh,
                },
                {
                    "name": "cosh",
                    "type": Cosh,
                },
                {
                    "name": "sinh",
                    "type": Sinh,
                },
                {
                    "name": "cot",
                    "type": Cot,
                },
                {
                    "name": "csc",
                    "type": Csc,
                },
                {
                    "name": "sec",
                    "type": Sec,
                },
                {
                    "name": "tan",
                    "type": Tan,
                },
                {
                    "name": "cos",
                    "type": Cos,
                },
                {
                    "name": "sin",
                    "type": Sin,
                },
                {
                    "name": "mode",
                    "type": Mode,
                },
                {
                    "name": "median",
                    "type": Median,
                },
                {
                    "name": "variance",
                    "type": Variance,
                },
                {
                    "name": "sdev",
                    "type": Sdev,
                },
                {
                    "name": "mean",
                    "type": Mean,
                },
                {
                    "name": "matrixrow",
                    "type": Matrixrow,
                },
                {
                    "name": "matrix",
                    "type": Matrix,
                },
                {
                    "name": "vector",
                    "type": Vector,
                },
                {
                    "name": "transpose",
                    "type": Transpose,
                },
                {
                    "name": "determinant",
                    "type": Determinant,
                },
                {
                    "name": "selector",
                    "type": Selector,
                },
                {
                    "name": "outerproduct",
                    "type": Outerproduct,
                },
                {
                    "name": "scalarproduct",
                    "type": Scalarproduct,
                },
                {
                    "name": "vectorproduct",
                    "type": Vectorproduct,
                },
                {
                    "name": "emptyset",
                    "type": Emptyset,
                },
                {
                    "name": "primes",
                    "type": Primes,
                },
                {
                    "name": "complexes",
                    "type": Complexes,
                },
                {
                    "name": "naturalnumbers",
                    "type": Naturalnumbers,
                },
                {
                    "name": "rationals",
                    "type": Rationals,
                },
                {
                    "name": "reals",
                    "type": Reals,
                },
                {
                    "name": "integers",
                    "type": Integers,
                },
                {
                    "name": "infinity",
                    "type": Infinity,
                },
                {
                    "name": "eulergamma",
                    "type": Eulergamma,
                },
                {
                    "name": "pi",
                    "type": Pi,
                },
                {
                    "name": "false",
                    "type": FalseType,
                },
                {
                    "name": "true",
                    "type": TrueType,
                },
                {
                    "name": "notanumber",
                    "type": Notanumber,
                },
                {
                    "name": "imaginaryi",
                    "type": Imaginaryi,
                },
                {
                    "name": "exponentiale",
                    "type": Exponentiale,
                },
                {
                    "name": "maction",
                    "type": Maction,
                },
                {
                    "name": "mlongdiv",
                    "type": Mlongdiv,
                },
                {
                    "name": "mstack",
                    "type": Mstack,
                },
                {
                    "name": "mtable",
                    "type": Mtable,
                },
                {
                    "name": "mmultiscripts",
                    "type": Mmultiscripts,
                },
                {
                    "name": "munderover",
                    "type": Munderover,
                },
                {
                    "name": "mover",
                    "type": Mover,
                },
                {
                    "name": "munder",
                    "type": Munder,
                },
                {
                    "name": "msubsup",
                    "type": Msubsup,
                },
                {
                    "name": "msup",
                    "type": Msup,
                },
                {
                    "name": "msub",
                    "type": Msub,
                },
                {
                    "name": "menclose",
                    "type": Menclose,
                },
                {
                    "name": "mfenced",
                    "type": Mfenced,
                },
                {
                    "name": "mphantom",
                    "type": Mphantom,
                },
                {
                    "name": "mpadded",
                    "type": Mpadded,
                },
                {
                    "name": "merror",
                    "type": Merror,
                },
                {
                    "name": "mstyle",
                    "type": Mstyle,
                },
                {
                    "name": "mroot",
                    "type": Mroot,
                },
                {
                    "name": "msqrt",
                    "type": Msqrt,
                },
                {
                    "name": "mfrac",
                    "type": Mfrac,
                },
                {
                    "name": "mrow",
                    "type": Mrow,
                },
                {
                    "name": "maligngroup",
                    "type": Maligngroup,
                },
                {
                    "name": "malignmark",
                    "type": Malignmark,
                },
                {
                    "name": "ms",
                    "type": Ms,
                },
                {
                    "name": "mspace",
                    "type": Mspace,
                },
                {
                    "name": "mtext",
                    "type": Mtext,
                },
                {
                    "name": "mo",
                    "type": Mo,
                },
                {
                    "name": "mn",
                    "type": Mn,
                },
                {
                    "name": "mi",
                    "type": Mi,
                },
                {
                    "name": "semantics",
                    "type": ForwardRef("Math.Semantics"),
                },
            ),
        },
    )
    mathcolor: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    scriptlevel: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    displaystyle: None | MathDisplaystyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scriptsizemultiplier: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scriptminsize: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    infixlinebreakstyle: None | MathInfixlinebreakstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    decimalpoint: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*\S\s*",
        },
    )
    accent: None | MathAccent = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accentunder: None | MathAccentunder = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | MathAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    alignmentscope: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    bevelled: None | MathBevelled = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charalign: None | MathCharalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charspacing: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    close: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    columnalign: list[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    columnspan: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    columnwidth: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    crossout: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    denomalign: None | MathDenomalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    depth: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    dir: None | MathDir = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    edge: None | MathEdge = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equalcolumns: None | MathEqualcolumns = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equalrows: None | MathEqualrows = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fence: None | MathFence = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: None | MathForm = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: None | Linestyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    framespacing: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        },
    )
    groupalign: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        },
    )
    height: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentalign: None | MathIndentalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignfirst: None | MathIndentalignfirst = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignlast: None | MathIndentalignlast = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshift: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentshiftfirst: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentshiftlast: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indenttarget: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    largeop: None | MathLargeop = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    leftoverhang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    length: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreak: None | MathLinebreak = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakmultchar: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakstyle: None | MathLinebreakstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lineleading: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    linethickness: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    location: None | MathLocation = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    longdivstyle: None | MathLongdivstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lquote: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lspace: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    mathsize: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    mathvariant: None | MathMathvariant = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxsize: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minlabelspacing: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minsize: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    movablelimits: None | MathMovablelimits = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mslinethickness: None | str | MathValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    notation: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    numalign: None | MathNumalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    open: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    position: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rightoverhang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rowalign: list[Verticalalign] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rowlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rowspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    rowspan: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rquote: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rspace: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    selection: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separator: None | MathSeparator = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separators: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    shift: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    side: None | MathSide = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stackalign: None | MathStackalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stretchy: None | MathStretchy = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subscriptshift: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    superscriptshift: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    symmetric: None | MathSymmetric = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
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
    display: None | MathDisplay = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxwidth: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    overflow: None | MathOverflow = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    altimg: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    altimg_width: None | str = field(
        default=None,
        metadata={
            "name": "altimg-width",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    altimg_height: None | str = field(
        default=None,
        metadata={
            "name": "altimg-height",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    altimg_valign: None | str | MathValue = field(
        default=None,
        metadata={
            "name": "altimg-valign",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    alttext: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cdgroup: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mode_attribute: None | str = field(
        default=None,
        metadata={
            "name": "mode",
            "type": "Attribute",
        },
    )
    macros: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Semantics:
        choice: (
            None
            | Apply
            | Bind
            | Ci
            | Cn
            | Csymbol
            | Cbytes
            | Cerror
            | Cs
            | Share
            | Piecewise
            | Declare
            | Fn
            | Reln
            | Interval
            | Moment
            | Log
            | Ln
            | Image
            | Codomain
            | Domain
            | Ident
            | Inverse
            | Lambda
            | Compose
            | Quotient
            | Divide
            | Minus
            | Power
            | Rem
            | Root
            | Factorial
            | Abs
            | Conjugate
            | Arg
            | Real
            | Imaginary
            | Floor
            | Ceiling
            | Exp
            | Min
            | Max
            | Lcm
            | Gcd
            | Times
            | Plus
            | Xor
            | Or
            | And
            | Not
            | Equivalent
            | Implies
            | Exists
            | Forall
            | Leq
            | Geq
            | Lt
            | Gt
            | Eq
            | Tendsto
            | Factorof
            | Approx
            | Neq
            | Int
            | Diff
            | Partialdiff
            | Laplacian
            | Curl
            | Grad
            | Divergence
            | List
            | Set
            | Cartesianproduct
            | Intersect
            | UnionType
            | Setdiff
            | Notprsubset
            | Notsubset
            | Notin
            | In
            | Prsubset
            | Subset
            | Card
            | Sum
            | Product
            | Limit
            | Arctanh
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
            | Mode
            | Median
            | Variance
            | Sdev
            | Mean
            | Matrixrow
            | Matrix
            | Vector
            | Transpose
            | Determinant
            | Selector
            | Outerproduct
            | Scalarproduct
            | Vectorproduct
            | Emptyset
            | Primes
            | Complexes
            | Naturalnumbers
            | Rationals
            | Reals
            | Integers
            | Infinity
            | Eulergamma
            | Pi
            | FalseType
            | TrueType
            | Notanumber
            | Imaginaryi
            | Exponentiale
            | Maction
            | Mlongdiv
            | Mstack
            | Mtable
            | Mmultiscripts
            | Munderover
            | Mover
            | Munder
            | Msubsup
            | Msup
            | Msub
            | Menclose
            | Mfenced
            | Mphantom
            | Mpadded
            | Merror
            | Mstyle
            | Mroot
            | Msqrt
            | Mfrac
            | Mrow
            | Maligngroup
            | Malignmark
            | Ms
            | Mspace
            | Mtext
            | Mo
            | Mn
            | Mi
            | Math.Semantics
        ) = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "apply",
                        "type": Apply,
                    },
                    {
                        "name": "bind",
                        "type": Bind,
                    },
                    {
                        "name": "ci",
                        "type": Ci,
                    },
                    {
                        "name": "cn",
                        "type": Cn,
                    },
                    {
                        "name": "csymbol",
                        "type": Csymbol,
                    },
                    {
                        "name": "cbytes",
                        "type": Cbytes,
                    },
                    {
                        "name": "cerror",
                        "type": Cerror,
                    },
                    {
                        "name": "cs",
                        "type": Cs,
                    },
                    {
                        "name": "share",
                        "type": Share,
                    },
                    {
                        "name": "piecewise",
                        "type": Piecewise,
                    },
                    {
                        "name": "declare",
                        "type": Declare,
                    },
                    {
                        "name": "fn",
                        "type": Fn,
                    },
                    {
                        "name": "reln",
                        "type": Reln,
                    },
                    {
                        "name": "interval",
                        "type": Interval,
                    },
                    {
                        "name": "moment",
                        "type": Moment,
                    },
                    {
                        "name": "log",
                        "type": Log,
                    },
                    {
                        "name": "ln",
                        "type": Ln,
                    },
                    {
                        "name": "image",
                        "type": Image,
                    },
                    {
                        "name": "codomain",
                        "type": Codomain,
                    },
                    {
                        "name": "domain",
                        "type": Domain,
                    },
                    {
                        "name": "ident",
                        "type": Ident,
                    },
                    {
                        "name": "inverse",
                        "type": Inverse,
                    },
                    {
                        "name": "lambda",
                        "type": Lambda,
                    },
                    {
                        "name": "compose",
                        "type": Compose,
                    },
                    {
                        "name": "quotient",
                        "type": Quotient,
                    },
                    {
                        "name": "divide",
                        "type": Divide,
                    },
                    {
                        "name": "minus",
                        "type": Minus,
                    },
                    {
                        "name": "power",
                        "type": Power,
                    },
                    {
                        "name": "rem",
                        "type": Rem,
                    },
                    {
                        "name": "root",
                        "type": Root,
                    },
                    {
                        "name": "factorial",
                        "type": Factorial,
                    },
                    {
                        "name": "abs",
                        "type": Abs,
                    },
                    {
                        "name": "conjugate",
                        "type": Conjugate,
                    },
                    {
                        "name": "arg",
                        "type": Arg,
                    },
                    {
                        "name": "real",
                        "type": Real,
                    },
                    {
                        "name": "imaginary",
                        "type": Imaginary,
                    },
                    {
                        "name": "floor",
                        "type": Floor,
                    },
                    {
                        "name": "ceiling",
                        "type": Ceiling,
                    },
                    {
                        "name": "exp",
                        "type": Exp,
                    },
                    {
                        "name": "min",
                        "type": Min,
                    },
                    {
                        "name": "max",
                        "type": Max,
                    },
                    {
                        "name": "lcm",
                        "type": Lcm,
                    },
                    {
                        "name": "gcd",
                        "type": Gcd,
                    },
                    {
                        "name": "times",
                        "type": Times,
                    },
                    {
                        "name": "plus",
                        "type": Plus,
                    },
                    {
                        "name": "xor",
                        "type": Xor,
                    },
                    {
                        "name": "or",
                        "type": Or,
                    },
                    {
                        "name": "and",
                        "type": And,
                    },
                    {
                        "name": "not",
                        "type": Not,
                    },
                    {
                        "name": "equivalent",
                        "type": Equivalent,
                    },
                    {
                        "name": "implies",
                        "type": Implies,
                    },
                    {
                        "name": "exists",
                        "type": Exists,
                    },
                    {
                        "name": "forall",
                        "type": Forall,
                    },
                    {
                        "name": "leq",
                        "type": Leq,
                    },
                    {
                        "name": "geq",
                        "type": Geq,
                    },
                    {
                        "name": "lt",
                        "type": Lt,
                    },
                    {
                        "name": "gt",
                        "type": Gt,
                    },
                    {
                        "name": "eq",
                        "type": Eq,
                    },
                    {
                        "name": "tendsto",
                        "type": Tendsto,
                    },
                    {
                        "name": "factorof",
                        "type": Factorof,
                    },
                    {
                        "name": "approx",
                        "type": Approx,
                    },
                    {
                        "name": "neq",
                        "type": Neq,
                    },
                    {
                        "name": "int",
                        "type": Int,
                    },
                    {
                        "name": "diff",
                        "type": Diff,
                    },
                    {
                        "name": "partialdiff",
                        "type": Partialdiff,
                    },
                    {
                        "name": "laplacian",
                        "type": Laplacian,
                    },
                    {
                        "name": "curl",
                        "type": Curl,
                    },
                    {
                        "name": "grad",
                        "type": Grad,
                    },
                    {
                        "name": "divergence",
                        "type": Divergence,
                    },
                    {
                        "name": "list",
                        "type": List,
                    },
                    {
                        "name": "set",
                        "type": Set,
                    },
                    {
                        "name": "cartesianproduct",
                        "type": Cartesianproduct,
                    },
                    {
                        "name": "intersect",
                        "type": Intersect,
                    },
                    {
                        "name": "union",
                        "type": UnionType,
                    },
                    {
                        "name": "setdiff",
                        "type": Setdiff,
                    },
                    {
                        "name": "notprsubset",
                        "type": Notprsubset,
                    },
                    {
                        "name": "notsubset",
                        "type": Notsubset,
                    },
                    {
                        "name": "notin",
                        "type": Notin,
                    },
                    {
                        "name": "in",
                        "type": In,
                    },
                    {
                        "name": "prsubset",
                        "type": Prsubset,
                    },
                    {
                        "name": "subset",
                        "type": Subset,
                    },
                    {
                        "name": "card",
                        "type": Card,
                    },
                    {
                        "name": "sum",
                        "type": Sum,
                    },
                    {
                        "name": "product",
                        "type": Product,
                    },
                    {
                        "name": "limit",
                        "type": Limit,
                    },
                    {
                        "name": "arctanh",
                        "type": Arctanh,
                    },
                    {
                        "name": "arcsinh",
                        "type": Arcsinh,
                    },
                    {
                        "name": "arcsech",
                        "type": Arcsech,
                    },
                    {
                        "name": "arcsec",
                        "type": Arcsec,
                    },
                    {
                        "name": "arccsch",
                        "type": Arccsch,
                    },
                    {
                        "name": "arccsc",
                        "type": Arccsc,
                    },
                    {
                        "name": "arccoth",
                        "type": Arccoth,
                    },
                    {
                        "name": "arccot",
                        "type": Arccot,
                    },
                    {
                        "name": "arccosh",
                        "type": Arccosh,
                    },
                    {
                        "name": "arctan",
                        "type": Arctan,
                    },
                    {
                        "name": "arccos",
                        "type": Arccos,
                    },
                    {
                        "name": "arcsin",
                        "type": Arcsin,
                    },
                    {
                        "name": "coth",
                        "type": Coth,
                    },
                    {
                        "name": "csch",
                        "type": Csch,
                    },
                    {
                        "name": "sech",
                        "type": Sech,
                    },
                    {
                        "name": "tanh",
                        "type": Tanh,
                    },
                    {
                        "name": "cosh",
                        "type": Cosh,
                    },
                    {
                        "name": "sinh",
                        "type": Sinh,
                    },
                    {
                        "name": "cot",
                        "type": Cot,
                    },
                    {
                        "name": "csc",
                        "type": Csc,
                    },
                    {
                        "name": "sec",
                        "type": Sec,
                    },
                    {
                        "name": "tan",
                        "type": Tan,
                    },
                    {
                        "name": "cos",
                        "type": Cos,
                    },
                    {
                        "name": "sin",
                        "type": Sin,
                    },
                    {
                        "name": "mode",
                        "type": Mode,
                    },
                    {
                        "name": "median",
                        "type": Median,
                    },
                    {
                        "name": "variance",
                        "type": Variance,
                    },
                    {
                        "name": "sdev",
                        "type": Sdev,
                    },
                    {
                        "name": "mean",
                        "type": Mean,
                    },
                    {
                        "name": "matrixrow",
                        "type": Matrixrow,
                    },
                    {
                        "name": "matrix",
                        "type": Matrix,
                    },
                    {
                        "name": "vector",
                        "type": Vector,
                    },
                    {
                        "name": "transpose",
                        "type": Transpose,
                    },
                    {
                        "name": "determinant",
                        "type": Determinant,
                    },
                    {
                        "name": "selector",
                        "type": Selector,
                    },
                    {
                        "name": "outerproduct",
                        "type": Outerproduct,
                    },
                    {
                        "name": "scalarproduct",
                        "type": Scalarproduct,
                    },
                    {
                        "name": "vectorproduct",
                        "type": Vectorproduct,
                    },
                    {
                        "name": "emptyset",
                        "type": Emptyset,
                    },
                    {
                        "name": "primes",
                        "type": Primes,
                    },
                    {
                        "name": "complexes",
                        "type": Complexes,
                    },
                    {
                        "name": "naturalnumbers",
                        "type": Naturalnumbers,
                    },
                    {
                        "name": "rationals",
                        "type": Rationals,
                    },
                    {
                        "name": "reals",
                        "type": Reals,
                    },
                    {
                        "name": "integers",
                        "type": Integers,
                    },
                    {
                        "name": "infinity",
                        "type": Infinity,
                    },
                    {
                        "name": "eulergamma",
                        "type": Eulergamma,
                    },
                    {
                        "name": "pi",
                        "type": Pi,
                    },
                    {
                        "name": "false",
                        "type": FalseType,
                    },
                    {
                        "name": "true",
                        "type": TrueType,
                    },
                    {
                        "name": "notanumber",
                        "type": Notanumber,
                    },
                    {
                        "name": "imaginaryi",
                        "type": Imaginaryi,
                    },
                    {
                        "name": "exponentiale",
                        "type": Exponentiale,
                    },
                    {
                        "name": "maction",
                        "type": Maction,
                    },
                    {
                        "name": "mlongdiv",
                        "type": Mlongdiv,
                    },
                    {
                        "name": "mstack",
                        "type": Mstack,
                    },
                    {
                        "name": "mtable",
                        "type": Mtable,
                    },
                    {
                        "name": "mmultiscripts",
                        "type": Mmultiscripts,
                    },
                    {
                        "name": "munderover",
                        "type": Munderover,
                    },
                    {
                        "name": "mover",
                        "type": Mover,
                    },
                    {
                        "name": "munder",
                        "type": Munder,
                    },
                    {
                        "name": "msubsup",
                        "type": Msubsup,
                    },
                    {
                        "name": "msup",
                        "type": Msup,
                    },
                    {
                        "name": "msub",
                        "type": Msub,
                    },
                    {
                        "name": "menclose",
                        "type": Menclose,
                    },
                    {
                        "name": "mfenced",
                        "type": Mfenced,
                    },
                    {
                        "name": "mphantom",
                        "type": Mphantom,
                    },
                    {
                        "name": "mpadded",
                        "type": Mpadded,
                    },
                    {
                        "name": "merror",
                        "type": Merror,
                    },
                    {
                        "name": "mstyle",
                        "type": Mstyle,
                    },
                    {
                        "name": "mroot",
                        "type": Mroot,
                    },
                    {
                        "name": "msqrt",
                        "type": Msqrt,
                    },
                    {
                        "name": "mfrac",
                        "type": Mfrac,
                    },
                    {
                        "name": "mrow",
                        "type": Mrow,
                    },
                    {
                        "name": "maligngroup",
                        "type": Maligngroup,
                    },
                    {
                        "name": "malignmark",
                        "type": Malignmark,
                    },
                    {
                        "name": "ms",
                        "type": Ms,
                    },
                    {
                        "name": "mspace",
                        "type": Mspace,
                    },
                    {
                        "name": "mtext",
                        "type": Mtext,
                    },
                    {
                        "name": "mo",
                        "type": Mo,
                    },
                    {
                        "name": "mn",
                        "type": Mn,
                    },
                    {
                        "name": "mi",
                        "type": Mi,
                    },
                    {
                        "name": "semantics",
                        "type": ForwardRef("Math.Semantics"),
                    },
                ),
            },
        )
        annotation_or_annotation_xml: list[Annotation | AnnotationXml] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "annotation",
                        "type": Annotation,
                    },
                    {
                        "name": "annotation-xml",
                        "type": AnnotationXml,
                    },
                ),
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
        cd: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        name: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
