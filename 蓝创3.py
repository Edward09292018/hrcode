from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = parse("data.xml")
root = DOMTree.documentElement
# html = etree.HTML(content)
print(root.nodeName)