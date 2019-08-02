import re


p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))


p = re.compile('(김원상)+')
m = p.search('김원상김원상 OK?')
print(m)

m = p.search('김원상김원상 개쩌는 김원상')
print(m)
print(m.group(0))
print(m.group(1))

