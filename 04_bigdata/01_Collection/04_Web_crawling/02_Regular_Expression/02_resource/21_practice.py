import re


def is_literal(sub_str, word):
    p = re.compile(word)
    s = p.findall(sub_str)
    if s:
        return s
    return None


testStr = 'Python exercises, PHP exercises, C# exercises'
patterns = 'exercises'

print(is_literal(testStr, patterns))
