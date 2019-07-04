# coding: cp949
infomation = """0 ~ 3세: 무료
4 ~ 13세: 2000원
14 ~ 18세: 3000원
19 ~ 65세: 5000원
66세 이상: 무료
"""
info_dictionary = {0:0,1:2000,2:3000,3:5000,4:0}
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
print("요금은 {0}원 입니다.".format(info_dictionary[customer_level]))
