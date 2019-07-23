from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))  # 현재노드의 속성 이름을 get의 인자로 넣어주면 속성의 값을 반환한다.
print(note.get("method"))  # 없는 속성에 대해서 None을 반환한다.
print(note.get("method", "gmail"))  # 없는 속성값에 대한 default값을 지정한다.
note.attrib["method"] = "gmail"  # 실제 속성 및 값 추가

print(note.keys())  # 해당노드의 모든 속성 이름을 리스트로 반환
print(note.items())  # 해당노드의 모든 속성과 값을 튜플형태로 반환

# 특정 노드의 전체 속성 값 출력
print("특정 노드의 전체 속성 값 출력")
for key in note.keys():
    print(note.get(key))

from_tag = note.find("From")
print(from_tag.text)

print("\n모든 자식의 노드 값 접근")
for parent in tree.getiterator():
    for child in parent:
        print(child.text)

print("특정 태그 자식 노드 접근")
for child in note.getiterator():
    print(child.text)
