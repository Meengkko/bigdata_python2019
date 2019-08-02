import re


def is_alphanumeric(sub_str):
    p = re.compile('123[\w]*')
    try:
        return p.search(sub_str).group().strip()
    except AttributeError:
        return None


print(is_alphanumeric('dfsajfkjeqwljivnvi034n023j4138tj0ngui3r0j0f480128123fdkslvfvkacsan923402##huid0wjcvio'))
print(is_alphanumeric('man LIFE a li3ve'))
