import re

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub("\g<phone> \g<name>", "park 010-1234-5678"))
