number_string = input("쉼표로 구분한 숫자 묶음을 입력하세요. (예, 65,45,2,3,45,8) : ")
print(sum(map(lambda x: int(x), number_string.split(','))))
