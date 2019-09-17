from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET

f = open('Korean2.xml', 'r', encoding='UTF-8')
text = f.read()
f.close()

print(text)

tree = ET.fromstring(text)
# root_node = tree.getroot()
node = Element("data")
node.text = "연습"
node.text = node.text.encode('UTF-8')
tree.append(node)
ET.ElementTree(tree).write('Korean.xml')