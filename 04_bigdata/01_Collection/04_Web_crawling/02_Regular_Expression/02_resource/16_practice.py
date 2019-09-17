import re


def is_alphanumeric(sub_str):
    p = re.compile('[1-9]*[.]')
    try:
        return p.search(sub_str).group().strip()
    except AttributeError:
        return None


print(is_alphanumeric('0192.0168.0001.0004'))
print(is_alphanumeric('192.168.0.1'))
