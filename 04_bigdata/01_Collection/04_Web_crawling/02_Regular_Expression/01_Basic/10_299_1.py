import re


def print_if_match(me):
    if me:
        print('Match found:', me.group())
    else:
        print('No match')


p = re.compile("[a-z]+")
m = p.match('python')
print_if_match(m)

m = p.match('3 python')
print_if_match(m)
