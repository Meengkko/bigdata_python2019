import re


def is_alphanumeric(sub_str):
    p = re.compile('[\w]+')
    try:
        return p.findall(sub_str)
    except AttributeError:
        return None


print(is_alphanumeric('Live a life 1 man'))
print(is_alphanumeric('man LIFE a li3ve'))
