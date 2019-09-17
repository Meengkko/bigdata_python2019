import re


p = re.compile(r'((\w+)\s+\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-5678')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))  # 매칭이 되는 그룹이 없기 때문에 에러
