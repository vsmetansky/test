from scraper.exporters import XmlAutoItemExporter


class XmlExportPipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.file_name, 'w')
        self.exporter = XmlAutoItemExporter(
            self.file, root_element='data')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
