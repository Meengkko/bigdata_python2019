import re

original_text = '''a1 sdajfklsdjfl
34 dsjkfhsdlfjlds
b3 fdskljfkalsdj
c4 fdlkwjeifskdl
9o vnfdmlsamcsdl
2e fklwermklmfkl
g5 fjdksljfakdfe
'''

p = re.compile('[a-zA-Z0-9][0-9]')
m = p.match(original_text)
print(m)

p = re.compile('[\d]')
m = p.match(original_text)
print(m)

p = re.compile('[\w][\d]')
m = p.match(original_text)
print(m)

p = re.compile('[\s][\d]')
m = p.match(' 1')
print(m)
m = p.match('\n1')
print(m)

p = re.compile('[\w]')
m = p.match('a')
print(m)
m = p.match('A')
print(m)
m = p.match('1')
print(m)
m = p.match('!')
print(m)
m = p.match('-')
print(m)
m = p.match(' ')
print(m)

p = re.compile('[\S]')
m = p.match('%')
print(m)
