import re


def is_literal(sub_str, word):
    p = re.compile(word)
    s = p.finditer(sub_str)
    if s:
        return s
    return None


testStr = 'Python exercises, PHP exercises, C# exercises'
patterns = 'exercises'

result = is_literal(testStr, patterns)

length = 0
for i in result:
    length += 1
print("occurrence: %d" % length)

for result_one in is_literal(testStr, patterns):
    print("position: ", result_one.span())
