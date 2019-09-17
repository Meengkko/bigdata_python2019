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
