import re


def is_alphanumeric(sub_str):
    p = re.compile('b{3}.+')
    try:
        return p.match(sub_str).group()
    except AttributeError:
        return None


print(is_alphanumeric('bbby kim'))
print(is_alphanumeric('b kim'))
print(is_alphanumeric(' kim'))
