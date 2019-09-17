import re

p = re.compile('[a-c]')
m = p.match('apple')
print(m)
m = p.match('travel')
print(m)

p = re.compile('[^0-9]')
m = p.match('iris2019')
print(m)
m = p.match('2iris2019')
print(m)
