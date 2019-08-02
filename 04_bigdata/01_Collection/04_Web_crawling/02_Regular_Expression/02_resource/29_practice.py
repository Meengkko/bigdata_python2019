import re


def digit_finder(sub_str):
    p = re.compile(r'\d+', re.MULTILINE)
    s = p.finditer(sub_str)
    if s:
        return s
    return None


sample_string = '''1fddf32f2-jkf2i3kd2j30dj02j3
fk3029f23d-32k-230dk4fj023i4jfi230d2
3k2d0293kd0k23d0wqqcwm0acm 
'''

[print(i.group(), i.span()) for i in digit_finder(sample_string)]
