class Restaurant:
    def __init__(self, name, types):
        self.restaurant_name = name
        self.cuisine_type = types
        self.number_served = 0

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다.\n" % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요\n" % self.restaurant_name)

    def reset_number_served(self):
        self.number_served = 0
        print("손님 카운팅을 0으로 초기화 하였습니다.\n")

    def increment_number_served(self, number):
        self.number_served += number
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다.\n" % number)

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n" % self.number_served)

    def __del__(self):
        print("%s 레스토랑 문닫습니다." %(self.restaurant_name))


rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split(" ")
opening_rest = Restaurant(rest_name, rest_type)
opening_rest.describe_restaurant()

while True:
    yesOrNo = (input("레스토랑을 오픈하시겠습니까? (y / n): ")).lower()
    if yesOrNo[0] == 'y':
        input_num = 0
        opening_rest.open_restaurant()
        while True:
            input_num = input("어서오세요. 몇명이십니까? (초기화:0, 입력종료:-1, 누적고객확인:p) : ")
            if input_num == 'p':
                opening_rest.check_customer_number()
            elif int(input_num) == 0:
                opening_rest.reset_number_served()
            elif int(input_num) == -1:
                break
            elif int(input_num) > 0:
                opening_rest.increment_number_served(int(input_num))
        del opening_rest
    elif yesOrNo[0] == 'n':
        break
    else:
        print("올바른 단어를 입력하세요")
        continue
