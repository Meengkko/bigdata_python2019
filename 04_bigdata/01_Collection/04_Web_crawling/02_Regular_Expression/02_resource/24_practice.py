import re


def find_date(sub_str):
    p = re.compile(r'\d+/\d+/\d+')
    s = p.search(sub_str)
    if s:
        return s.group()
    return None


sample_url = 'https://www.washingtonpost.com/politics/2019/07/31/6e852816-b27b-11e9-8f6c-7828e68cb15f_story.html?utm_term=.a99d2852ac55'
print(find_date(sample_url))
