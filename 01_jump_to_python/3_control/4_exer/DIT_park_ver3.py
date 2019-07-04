# coding: cp949
infomation = """
====I N F O M A T I O N====
  0 ~ 3세(유  아): 무료
 4 ~ 13세(어린이): 2000원
14 ~ 18세(청소년): 3000원
19 ~ 65세(성  인): 5000원
66세 이상(노  인): 무료
===========================
"""

info_dictionary = {0:[0, "유아"],1:[2000, "어린이"],2:[3000, "청소년"],3:[5000, "성인"],4:[0, "노인"]}

customer_age = -1

while True:
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
        print("다시 입력하세요\n")
        continue
    print("귀하는 {0}등급이며 요금은 {1}원 입니다.\n".format(info_dictionary[customer_level][1], info_dictionary[customer_level][0]))

    checkIn = int(input("요금을 입력하세요."))
    if checkIn < info_dictionary[customer_level][0]:
        print("%d원이 모자랍니다. 입력하신 %d원을 반납합니다." % ((((info_dictionary[customer_level][0]) - checkIn), checkIn)))
    else:
        if checkIn == info_dictionary[customer_level][0]:
            print("감사합니다. 티켓을 발행합니다.")
        else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % ((checkIn - (info_dictionary[customer_level][0]))))

