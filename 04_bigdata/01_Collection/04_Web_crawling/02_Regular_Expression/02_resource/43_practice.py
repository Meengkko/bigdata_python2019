import re


def five_long(sub_str):
    p = re.compile(r'.*://.*[.].*[.][\w]+/', re.MULTILINE)
    s = p.search(sub_str)
    if s:
        return s.group()
    return None


sample_string ='https://www.washingtonpost.com/politics/2019/07/31/6e852816-b27b-11e9-8f6c-7828e68cb15f_story.html?utm_term=.a99d2852ac55'
print(five_long(sample_string))
