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
#info_dictionary = {"유아":0,"어린이":2000,"청소년":3000,"성인":5000,"노인":0}
coupons = {0:[5, "무료 티켓"], 1:[3, "할인 티켓"]}
customer_counter = 0
is_perchased = False

while True:
    print(infomation)
    customer_age = int(input("나이를 입력하세요.")) 
    if customer_age in range(0, 4):
        customer_level = 0
#        customer_level = '유아'
    elif customer_age in range(4, 14):
        customer_level = 1
    elif customer_age in range(14, 19):
        customer_level = 2
    elif customer_age in range(19, 66):
        customer_level = 3
    elif customer_age >=66:
        customer_level = 4
    else:
        print("다시 입력하세요\n")
        continue
    print("\n귀하는 {0}등급이며 요금은 {1}원 입니다.".format(info_dictionary[customer_level][1], info_dictionary[customer_level][0]))
    cashOrCredit = int(input("\n요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드)"))
    if cashOrCredit == 1:
        checkIn = int(input("\n요금을 입력하세요."))
        if checkIn < info_dictionary[customer_level][0]:
            print("\n%d원이 모자랍니다. 입력하신 %d원을 반납합니다." % (((info_dictionary[customer_level][0]) - checkIn), checkIn))
        else:
            is_perchased = True
            if checkIn == info_dictionary[customer_level][0]:
                print("\n감사합니다. 티켓을 발행합니다.")
            else:
                print("\n감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (checkIn - (info_dictionary[customer_level][0])))
    elif cashOrCredit == 2:
        is_perchased = True
        credit_pay = info_dictionary[customer_level][0] * 0.9
        if customer_age in range(60, 66):
            credit_pay *= 0.95
        print("\n%.0f원 결제 되었습니다. 티켓을 발행합니다." % (credit_pay))

    if is_perchased and customer_level != 0 and customer_level != 4:
        customer_counter += 1
        if customer_counter % 7 == 0 and coupons[0][0] != 0:
            coupons[0][0] = coupons[0][0] - 1
            print("\n축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장" % coupons[0][0])
        elif customer_counter % 4 == 0 and coupons[1][0] != 0:
            coupons[1][0] = coupons[1][0] - 1
            print("\n축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % coupons[1][0])
        is_perchased = False
