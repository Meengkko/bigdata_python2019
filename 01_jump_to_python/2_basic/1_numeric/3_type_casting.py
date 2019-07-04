# coding: cp949
a = 1
print(a)

b = 2.5
result = a+b
print(result)       # 정수와 실수형의 연산시 그 결과가 실수형으로 확장된다.

c = 0.75
result = a/c
print(result)       # 같은 숫자형내의 / 연산시 그 결과가 실수형으로 확장된다.

b = "Hello World"  
result = a+b        # 문자열 형과 숫자형의 + 연산은 정의되어 있지 않다.
print(result)
