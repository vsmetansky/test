from scrapy.exporters import XmlItemExporter
from xml.sax.saxutils import XMLGenerator


class XmlAutoItemExporter(XmlItemExporter):
    def start_exporting(self):
        self.xg.startDocument()
        self.__add_xsl_link()
        self.xg.startElement(self.root_element, {})
        self._beautify_newline(new_item=True)

    def __add_xsl_link(self):
        self.xg._write(
            f'<?xml-stylesheet type="text/xsl" href="map.xsl"?>')
