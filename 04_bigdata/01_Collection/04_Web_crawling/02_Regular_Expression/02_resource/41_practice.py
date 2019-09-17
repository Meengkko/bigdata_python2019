import re


def five_long(sub_str):
    p = re.compile(r'[^a-zA-Z]', re.MULTILINE)
    s = p.sub('', sub_str)
    if s:
        return s
    return None


sample_string ='dsjakf233490gjiewj0c23jic00(#)!@JI)WNDI)!J)#DJ!@JDI)CJ@#290318'
print(five_long(sample_string))
