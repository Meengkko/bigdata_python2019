import re

p = re.compile('blue|white|red')
print(p.sub('colour', 'blue socks and red socks'))
print(p.sub('colour', 'blue socks and red socks', count=1))
