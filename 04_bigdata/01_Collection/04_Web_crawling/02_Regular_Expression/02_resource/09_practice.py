import re


def is_alphanumeric(sub_str):
    p = re.compile('[a].*[b]')
    try:
        return p.search(sub_str).group()
    except AttributeError:
        return None


print(is_alphanumeric(' aDfdscb'))
print(is_alphanumeric('fsdaklDksdvj fdjkslfjb_fd fdk'))
print(is_alphanumeric('340f9GGkajsadasl043i0jvbkj_fd0'))
