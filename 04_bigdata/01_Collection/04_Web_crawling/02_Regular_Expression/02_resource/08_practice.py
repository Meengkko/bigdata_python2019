import re


def is_alphanumeric(sub_str):
    p = re.compile('[A-Z][a-z]+')
    try:
        return p.search(sub_str).group()
    except AttributeError:
        return None


print(is_alphanumeric(' dd_fe Dfdsc'))
print(is_alphanumeric('fsdklDksdvj fdjkslfj_fd fdk'))
print(is_alphanumeric('340f9GGkjsadasl043i0jvkj_fd0'))
