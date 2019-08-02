import re
pattern = re.compile('[abc]')
match_result = pattern.match('a')
print(match_result)

match_result = pattern.match('before')
print(match_result)

match_result = pattern.match('dude')
print(match_result)

match_result = pattern.match('sang')
print(match_result)

match_result = pattern.search('sang')
print(match_result)

s_pattern = re.compile('s[abc]')
# 기본 정규식 문법을 적용하였을 경우
# 문자열 클래스는 매칭이되는 순서를 고려해야 한다.
match_result = s_pattern.match('sang')
print(match_result)

s_pattern = re.compile('s[abc]')
# 정규표현식을 대소문자를 구분한다.
match_result = s_pattern.match('Sang')
print(match_result)
