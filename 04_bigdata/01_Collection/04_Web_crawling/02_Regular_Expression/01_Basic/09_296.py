import re

p = re.compile('ca+t')
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat')
print(m)

p = re.compile('goo+gle')
m = p.match('gogle')
print(m)
m = p.match('google')
print(m)
m = p.match('gooooooooooooooooooooooooooooooooooooooooogle')
print(m)
