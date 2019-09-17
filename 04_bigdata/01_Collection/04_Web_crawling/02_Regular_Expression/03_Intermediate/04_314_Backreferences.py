import re
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring. It It was really great').group()
print(m)
