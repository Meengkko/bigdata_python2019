import re
p = re.compile("[a-z]+")
m = p.search("5 python")
result = m.start() + m.end()
print(result)
