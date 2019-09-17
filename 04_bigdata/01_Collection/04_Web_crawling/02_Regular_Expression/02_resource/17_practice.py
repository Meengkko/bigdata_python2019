import re


def is_alphanumeric(sub_str):
    p = re.compile('[0-9]+$')
    try:
        return p.search(sub_str).group().strip()
    except AttributeError:
        return None


print(is_alphanumeric('fhsdjkasdfl032'))
print(is_alphanumeric('fdmsaklvm213'))
