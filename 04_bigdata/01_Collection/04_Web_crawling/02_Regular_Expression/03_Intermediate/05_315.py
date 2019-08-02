import re


p = re.compile(r'(?P<name>\w+)\s+(?P<whole_number>(?P<first_numbers>\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-5678')
print(m.group("name"))
print(m.group(1))
print(m.group("whole_number"))
print(m.group(2))
print(m.group("first_numbers"))
print(m.group(3))

p = re.compile(r'''
(?P<name>\w+)\s+
(?P<first_number>\d+)
[-]
(?P<second_number>\d+)
[-]
(?P<third_number>\d+)
''', re.VERBOSE)

m = p.search('park 010-1234-5678')
print(m.group("name"))
print(m.group("first_number"))
print(m.group("second_number"))
print(m.group("third_number"))

