# coding: cp949
infomation = """0 ~ 3세(유아): 무료
4 ~ 13세(어린이): 2000원
14 ~ 18세(청소년): 3000원
19 ~ 65세(성인): 5000원
66세 이상(노인): 무료
"""

info_dictionary = {0:[0, "유아"],1:[2000, "어린이"],2:[3000, "청소년"],3:[5000, "성인"],4:[0, "노인"]}

customer_age = -1

while customer_age < 0:
    print(infomation)
    customer_age = int(input("나이를 입력하세요.")) 
    if customer_age >=0 and customer_age <= 3:
        customer_level = 0
    elif customer_age >=4 and customer_age <= 13:
        customer_level = 1
    elif customer_age >=14 and customer_age <= 18:
        customer_level = 2
    elif customer_age >=19 and customer_age <= 65:
        customer_level = 3
    elif customer_age >=66:
        customer_level = 4
    else:
        print("다시 입력하세요")

print("귀하는 {0}등급이며 요금은 {1}원 입니다.".format(info_dictionary[customer_level][1], info_dictionary[customer_level][0]))
