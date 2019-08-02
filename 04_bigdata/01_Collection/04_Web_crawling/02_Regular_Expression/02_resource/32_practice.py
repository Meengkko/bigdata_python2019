import re


def abbreviator(sub_str):
    p = re.compile('[ ,.]', re.MULTILINE)
    s = p.sub(':', sub_str, count=2)
    if s:
        return s
    return None


sample_string = '''We are not living in a world
where all Roads are radii of a circle and where all, 
if followed long enough, will therefore draw gradually
nearer and finally meet at the centre: rather in a world
where every Road, after a few miles, forks into two, and
each of those into two again, and at each fork, you must make a decision.'''

print(abbreviator(sample_string))
