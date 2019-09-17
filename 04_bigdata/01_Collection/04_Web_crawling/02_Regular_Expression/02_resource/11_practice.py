import re


def is_alphanumeric(sub_str):
    p = re.compile('[\w]+$')
    try:
        return p.search(sub_str).group().strip()
    except AttributeError:
        return None


print(is_alphanumeric('live a life'))
print(is_alphanumeric(' life a live'))
