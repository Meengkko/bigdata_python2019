import re


def is_alphanumeric(sub_str):
    p = re.compile('[a-z]+[_][a-z]+')
    try:
        return p.search(sub_str).group()
    except AttributeError:
        return None


print(is_alphanumeric(' dd_fe fdsc'))
print(is_alphanumeric('fsdklksdvj fdjkslfj_fd fdk'))
print(is_alphanumeric('340f9kj043i0jvkj_fd0'))
