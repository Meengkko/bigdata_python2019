import re


def five_long(sub_str):
    p = re.compile(r'\b\w{4,}\b', re.MULTILINE)
    s = p.findall(sub_str)
    if s:
        return s
    return None


sample_string = '''We are not living in a world
where all Roads are radii of a circle and where all, 
if followed long enough, will therefore draw gradually
nearer and finally meet at the centre: rather in a world
where every Road, after a few miles, forks into two, and
each of those into two again, and at each fork, you must make a decision.'''

print(five_long(sample_string))
