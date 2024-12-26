"""

for var, val in XmlSerializer.next_value(item.qti_item_body, meta):
    print(var)
    print(val)
"""
import argparse
import code
import resource
from io import StringIO

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem


def load_item(file):
    return XmlParser().parse(file, QtiAssessmentItem)

#def load_file(filename):
#    with open(filename, "rb") as file_data:
#        return load_item(file_data)

def render_to_text(qti_assessment_item: QtiAssessmentItem):
    buffer = StringIO()
    buffer.write(qti_assessment_item.title)
    return buffer.getvalue()

def render_to_html(qti_assessment_item: QtiAssessmentItem):
    return "Pretend I'm legit HTML output"

def render_to_xml(model):
    # This currently only does the right thing for QtiAssessmentItem
    serializer_config = SerializerConfig(
        indent="  ",
        ignore_default_attributes=True,
    )
    serializer = XmlSerializer(config=serializer_config)
    xml_text = serializer.render(
        model,
        ns_map={None: "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"}
    )
    return xml_text

def main():
    parser = argparse.ArgumentParser(
        prog="pyqti.render",
        description="Render QTI assessment items in different formats."
    )
    parser.add_argument('format', choices=['html', 'text', 'xml'])
    parser.add_argument('file', type=argparse.FileType('rb'))
    parser.add_argument('--stats', action="store_true", default=False)
    parser.add_argument('--interactive', action="store_true", default=False)
    args = parser.parse_args()
    item = load_item(args.file)

    renderers = {
        'html': render_to_html,
        'text': render_to_text,
        'xml': render_to_xml,
    }
    output_text = renderers[args.format](item)
    print(output_text)

    if args.stats:
        print("\n------ Stats ------")
        mb_memory_used = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1_000_000.0, 2)
        print(f"Memory Usage: {mb_memory_used} MB")

    if args.interactive:
        code.interact(
            local={
                'item': item,
            }
        )

if __name__ == "__main__":
    main()
