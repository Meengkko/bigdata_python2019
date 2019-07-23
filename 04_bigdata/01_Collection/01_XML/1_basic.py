from xml.etree.ElementTree import Element, dump

note = Element('note')

to = Element('to')  # 자식 노드
to.text = "Tove"  # 현재 앨리먼트(Tag)에 값 추가
note.append(to)  # 부모 노드에 자식노드 추가

dump(note)
dump(to)
