class Restaurant:
    def __init__(self, name, types):
        self.restaurant_name = name
        self.cuisine_type = types
        self.today_customer = 0
        try:
            with open("./customer_file/고객서빙현황로그.txt", 'r', encoding='UTF-8') as customer_f:
                customer_log = ((customer_f.readlines())[-1].split("\t"))[1]
                self.number_served = int(customer_log)
        except FileNotFoundError:
            self.number_served = 0
            # with open("./customer_file/고객서빙현황로그.txt", 'w', encoding='UTF-8') as customer_f:
            #     customer_f.write("손님수\t누적손님수\t\n")
            #     self.number_served = 0

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다.\n" % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요\n" % self.restaurant_name)

    def reset_number_served(self):
        self.today_customer = 0
        print("손님 카운팅을 0으로 초기화 하였습니다.\n")

    def increment_number_served(self, number):
        self.today_customer += number
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다.\n" % number)

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n" % self.today_customer)

    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.restaurant_name)
        self.number_served += self.today_customer
        with open("./customer_file/고객서빙현황로그.txt", 'a', encoding='UTF-8') as customer_f:
            customer_f.write("%d\t%d\n" % (self.today_customer, self.number_served))


rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split(" ")
opening_rest = Restaurant(rest_name, rest_type)
opening_rest.describe_restaurant()
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
