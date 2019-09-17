import re


def digit_finder(sub_str):
    p = re.compile(r'\d+', re.MULTILINE)
    s = p.findall(sub_str)
    if s:
        return s
    return None


sample_string = ''' 1. Kim
2. Lee
3. Park
...
109. Fah
'''

[print(i, end=' ') for i in digit_finder(sample_string)]
