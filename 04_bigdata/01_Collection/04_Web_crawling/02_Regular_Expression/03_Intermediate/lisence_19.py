import re

yellow_book = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

p = re.compile("(\w+\s\d+[-]\d+[-])\d+")
print(p.sub("\g<1>####", yellow_book))
