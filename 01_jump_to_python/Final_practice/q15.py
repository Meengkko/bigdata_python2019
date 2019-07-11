input_numstr = input("띄어쓰기로 구분한 숫자로된 문자열을 입력하시오").split(' ')
for i in range(len(input_numstr)):
    listed_numbers = list(input_numstr[i])
    if len(listed_numbers) == len(set(listed_numbers)):
        print("true", end=' ')
    else:
        print('false', end=' ')
