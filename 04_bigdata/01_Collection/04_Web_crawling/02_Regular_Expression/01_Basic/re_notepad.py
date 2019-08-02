import re
p = re.compile('\d{3}-\D{2}')
m = p.match('123-df')
print(m)

p = re.compile('ab?c')
m = p.match('ac')
print(m)
m = p.match('abbc')
print(m)
m = p.match('abcd')
print(m)


p = re.compile('[a-z]+')
m = p.match('python')
print(m)

source = "Luke Skywalker 02-123-4567 luke@daum.net"
m1 = re.findall('\w', source)
m2 = re.findall('[\w]+', source)
print("m1 :", m1)
print("m2 :", m2)
