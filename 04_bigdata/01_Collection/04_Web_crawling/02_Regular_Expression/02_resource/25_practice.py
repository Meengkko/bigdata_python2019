import re


def switch_date(sub_str):
    p = re.compile(r'(\d+)[-](\d+)[-](\d+)')
    s = p.sub("\g<3>-\g<2>-\g<1>", sub_str)
    if s:
        return s
    return None


sample_date = '2019-08-01'
print(switch_date(sample_date))
