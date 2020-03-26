from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from lxml import etree

XML_NAME = 'data.xml'
XHTML_NAME = 'data.xhtml'
MAP_NAME = 'map.xsl'
ITEM_NUM = 20


def apply_map(f_name, map):
    tree = etree.parse(f_name)
    xslt = etree.parse(map)
    return etree.XSLT(xslt)(tree)


def write_tree(f_name, tree):
    tree_s = etree.tostring(tree)
    with open(f_name, 'wb') as f:
        f.write(tree_s)


def xml_to_xhtml():
    tree = apply_map(XML_NAME, MAP_NAME)
    write_tree(XHTML_NAME, tree)


def start():
    process = CrawlerProcess(get_project_settings())

    process.crawl('auto_spider',
                  item_num=ITEM_NUM, file_name=XML_NAME)
    process.start()

    xml_to_xhtml()


if __name__ == '__main__':
    start()
