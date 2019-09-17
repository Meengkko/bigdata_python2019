import re


def five_long(sub_str):
    p = re.compile(r'"(.*?)"', re.MULTILINE)
    s = p.search(sub_str)
    if s:
        return s.group()
    return None


sample_string ='I told you "Know yourself" not'
print(five_long(sample_string))
