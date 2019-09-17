import re

original_text = "life is too short"

p = re.compile('[a-z]+')

m = p.search(original_text)
print(m.group())

m = p.findall(original_text)
print(m)
[print(word, end=' ') for word in m]
