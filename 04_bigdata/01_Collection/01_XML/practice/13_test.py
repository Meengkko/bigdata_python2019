from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET

f = open('students_info.xml', 'r', encoding='utf-8')
text = f.read()
f.close()

print(text)

root_node = ET.fromstring(text)
print(root_node.keys())

for student in root_node.getiterator():
    #print(student.keys())
    print(student.text)
