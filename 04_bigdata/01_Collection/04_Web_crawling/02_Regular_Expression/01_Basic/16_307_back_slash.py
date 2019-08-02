import re

# p = re.compile('\') <== 정규식으로 표현이 불가능하다.
# p = re.compile('\\') <== 이 역시 불가능하다.
p = re.compile('\\\\')

m = p.match('\\section')
print(m)

p = re.compile(r'\\')
m = p.match('\\section')
print(m)
p = re.compile(r'\\')
m = p.match('\\\\section')
print(m)
print(m.group())
