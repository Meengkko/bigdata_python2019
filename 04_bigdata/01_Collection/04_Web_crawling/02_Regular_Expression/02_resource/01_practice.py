import re


def is_alphanumeric(sub_str):
    p = re.compile('[\w]+')
    if p.match(sub_str) and sub_str == p.match(sub_str).group():
        return True
    return False


print(is_alphanumeric('ABCDEFabcdef123450'))
print(is_alphanumeric('*&%@#!}{'))
