import re


def two_words_of_p(sub_str):
    p = re.compile(r'P.+\sP.+')
    s = p.match(sub_str)
    if s:
        return s.group()
    return None


sample_string = ['Python Pie', 'Papa Push', 'Power Overwhelming']
for string in sample_string:
    print(two_words_of_p(string))
