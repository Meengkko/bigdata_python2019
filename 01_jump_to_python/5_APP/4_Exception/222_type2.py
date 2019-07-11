print('작업1')
num1 = 2
num2 = 0
try:
    result = num1 / num2
    f = open("나없는파일", 'r')
except ZeroDivisionError:
    print("분모가 0인 나누기를 수행하고 있습니다.")
    print("알고리즘 수행을 생략하고 다음 단계 진행합니다.")
except FileNotFoundError:
    print(''''나없는파일'이 없습니다.
파일을 준비하고 다시 수행하십시오.''')
print('작업2')
print('프로그램 정상종료')