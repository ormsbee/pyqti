"""
A very simple, temporary script to measure model loading & parsing overhead.

Nothing here may import anything from pyqti at module scope: importing the package
would pull in whatever those modules touch and the "before model import" reading
would already include it. ``pyqti/__init__.py`` resolves its exports lazily for the
same reason, so ``import pyqti`` on its own stays cheap.
"""

import resource
import sys
from datetime import datetime
from pathlib import Path

QTI_NAMESPACE = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
DEFAULT_EXAMPLE = Path(__file__).resolve().parents[3] / "examples" / "firstexample.xml"


def get_mem_usage():
    # ru_maxrss is kilobytes on Linux but bytes on macOS/BSD. Dividing by 1e6
    # unconditionally (as this script used to) under-reports by 1000x on Linux, which
    # is where the README's "around 38 MB" figure came from being measured elsewhere.
    scale = 1_000_000 if sys.platform == "darwin" else 1_000
    mib = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / scale, 2)
    return f"{mib} MB"


def main():
    example = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EXAMPLE

    print(f"Before xsdata bindings:          {get_mem_usage()}")
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.parsers.config import ParserConfig

    parser = XmlParser(config=ParserConfig(fail_on_converter_warnings=True))

    print(f"Before model import:             {get_mem_usage()}")
    from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem

    print(f"After model import:              {get_mem_usage()}")

    with example.open("rb") as xml_data:
        before = datetime.now()
        assessment_item = parser.parse(xml_data, QtiAssessmentItem)
        after = datetime.now()

    print(f"After parsing:                   {get_mem_usage()}")
    print(f"Parse time:                      {after - before}")

    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    serializer = XmlSerializer(
        config=SerializerConfig(indent="  ", ignore_default_attributes=True)
    )
    print()
    print(serializer.render(assessment_item, ns_map={None: QTI_NAMESPACE}))


if __name__ == "__main__":
    main()
