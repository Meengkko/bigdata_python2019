import re


def is_alphanumeric(sub_str):
    p = re.compile('\B[\w]*z[\w]*\B')
    try:
        return p.search(sub_str).group().strip()
    except AttributeError:
        return None


print(is_alphanumeric('liveza life'))
print(is_alphanumeric(' lifeza live'))
