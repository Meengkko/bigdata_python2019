import re


def is_alphanumeric(sub_str):
    p = re.compile('b+.+')
    try:
        return p.match(sub_str).group()
    except AttributeError:
        return None


print(is_alphanumeric('bbbbbbbbbobby kim'))
print(is_alphanumeric(' kim'))
