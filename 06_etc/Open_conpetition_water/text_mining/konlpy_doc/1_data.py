from konlpy.corpus import kolaw
from konlpy.corpus import kobill
c = kolaw.open('constitution.txt').read()
print(c[:10])

d = kobill.open('1809890.txt').read()
print(d[:15])
