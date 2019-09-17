import re

# DOTALL
print("DOTALL option")
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
# p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)
print("\nIGNORECASE option")

# IGNORECASE
p = re.compile('[a-z]+', re.IGNORECASE)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
m = p.match('PYTHON')
print(m)

# MULTILINE
print("\nMULTILINE option")
p = re.compile("^python\s\w+", re.MULTILINE)
data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data))
