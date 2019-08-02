import re

p = re.compile('.')  # 모든 문자클래스와 매칭이 된다.
                     # [] 문자열 클래스가 아닌 일반 문법으로 사용했을 경우
                     # '.'은 '줄바꿈을 제외한' 모든 문자를 의미하는 메타문자로 활용된다.
m = p.match('%')
print(m)

m = p.match('\n')
print(m)


p = re.compile('a.b')
m = p.match('a+b')
print(m)

m = p.match('a0b')
print(m)

m = p.match('a#b')
print(m)

m = p.match('a@b')
print(m)

p = re.compile('a[.]b')
m = p.match('a+b')
print(m)

p = re.compile('a..[.]txt')
m = p.match('abc.txt')
print(m)

p = re.compile('...')
m = p.match('hey man')
print(m)
