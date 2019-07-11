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

info_dictionary = {"유아":0,"어린이":2000,"청소년":3000,"성인":5000,"노인":0}
coupons = {"무료 티켓":5, "할인 티켓":3}
customer_counter = 0
is_perchased = False

while True:
    print(infomation)
    customer_age = int(input("나이를 입력하세요.")) 
    if customer_age in range(0, 4):
        customer_level = '유아'
    elif customer_age in range(4, 14):
        customer_level = '어린이'
    elif customer_age in range(14, 19):
        customer_level = '청소년'
    elif customer_age in range(19, 66):
        customer_level = '성인'
    elif customer_age >=66:
        customer_level = '노인'
    else:
        print("다시 입력하세요\n")
        continue
    print("\n귀하는 {0}등급이며 요금은 {1}원 입니다.".format(customer_level, info_dictionary[customer_level]))
    cashOrCredit = int(input("\n요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드)"))
    if cashOrCredit == 1:
        checkIn = int(input("\n요금을 입력하세요."))
        if checkIn < info_dictionary[customer_level]:
            print("\n%d원이 모자랍니다. 입력하신 %d원을 반납합니다." % (((info_dictionary[customer_level]) - checkIn), checkIn))
        else:
            is_perchased = True
            if checkIn == info_dictionary[customer_level]:
                print("\n감사합니다. 티켓을 발행합니다.")
            else:
                print("\n감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (checkIn - (info_dictionary[customer_level])))
    elif cashOrCredit == 2:
        is_perchased = True
        credit_pay = info_dictionary[customer_level] * 0.9
        if customer_age in range(60, 66):
            credit_pay *= 0.95
        print("\n%.0f원 결제 되었습니다. 티켓을 발행합니다." % (credit_pay))

    if is_perchased and customer_level not in ['유아', '노인']:
        customer_counter += 1
        print("\n%d번째 고객" % customer_counter)
        if customer_counter % 7 == 0 and coupons["무료 티켓"] != 0:
            coupons["무료 티켓"] = coupons["무료 티켓"] - 1
            print("\n축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장" % coupons["무료 티켓"])
        elif customer_counter % 4 == 0 and coupons["할인 티켓"] != 0:
            coupons["할인 티켓"] = coupons["할인 티켓"] - 1
            print("\n축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % coupons["할인 티켓"])
        is_perchased = False
