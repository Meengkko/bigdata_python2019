import re


def is_literal(sub_str, word):
    p = re.compile(word)
    s = p.search(sub_str)
    if s:
        return s.group(), s.span()
    return None


testStr = 'The quick brown fox jumps over the lazy dog.'
patterns = ['fox', 'dog', 'horse']

for words in patterns:
    print(is_literal(testStr, words))
