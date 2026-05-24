"""
A very simple, temporary script to measure model loading & parsing overhead.
"""
from pprint import pp
from datetime import datetime
import resource


def get_mem_usage():
    mib = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1_000_000.0, 2)
    return f"{mib} MiB"

def main():
    print(f"Before xsdata_pydantic bindings: {get_mem_usage()}")
    #from xsdata_pydantic.bindings import XmlParser
    from xsdata.formats.dataclass.parsers import XmlParser
    parser = XmlParser()

    print(f"Before model import: {get_mem_usage()}")
    from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem

    print(f"After model import: {get_mem_usage()}")

    #with open("adaptive-item.xml", "rb") as xml_data:
    with open("examples/firstexample.xml", "rb") as xml_data:
        before = datetime.now()
        assessment_item = parser.parse(xml_data, QtiAssessmentItem)
        after = datetime.now()
        print(f"After parsing: {get_mem_usage()}")
        parse_time = after - before
        print(parse_time)

    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    serializer_config = SerializerConfig(
        indent="  ",
        ignore_default_attributes=True,
    )
    serializer = XmlSerializer(config=serializer_config)
    xml_text = serializer.render(
        assessment_item,
        ns_map={None: "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"}
    )
    print(xml_text)
    #breakpoint()

if __name__ == "__main__":
    main()