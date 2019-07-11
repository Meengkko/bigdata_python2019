import time
import random

class Restaurant:
    def __init__(self, name):
        pass
    
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다. 어서오세요\n" % (self.restaurant_name, self.cuisine_type))

    def reset_number_served(self):
        self.today_customer = 0
        self.today_income = 0
        print("손님 카운팅과 오늘 수입을 0으로 초기화 하였습니다.\n")

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n" % self.today_customer)

    def __del__(self):
        print("%s 문닫습니다." %self.restaurant_name)

class KoreanRest(Restaurant):

    def __init__(self, name):
        self.restaurant_name = name
        self.get_menu = [0,0,0]
        self.KoreanMenu = {'김치찌개': 4000, '제육정식': 5000, '생선정식': 6000}
        self.cuisine_type = '한식'
        self.today_customer = 0
        self.today_income = 0
        self.total_income = 0

    def reset_number_served(self):
        self.today_customer = 0
        self.today_income = 0
        self.get_menu = [0,0,0]
        print("손님 카운팅과 오늘 수입을 0으로 초기화 하였습니다.\n")

    def take_order(self, order_list):
        self.today_income += sum(list(map(lambda x, y: x * y, list(self.KoreanMenu.values()), order_list)))
        self.today_customer += sum(order_list)
        self.get_menu = list(map(lambda x: sum(x), zip(self.get_menu, order_list)))

    def accounting_kor(self, today_date):
        try:
            with open("한식회계장부.txt", 'r', encoding='UTF-8') as kor_f:
                self.total_income = int(((kor_f.readlines())[-1].split("\t"))[-1]) + self.today_income
            with open("한식회계장부.txt", 'a', encoding='UTF-8') as kor_f:
                kor_f.write("%s\t%d\t%d\t%d\t%d\t%d\n"
                            % (today_date, self.get_menu[0], self.get_menu[1], self.get_menu[2], self.today_income, self.total_income))

        except:
            with open("한식회계장부.txt", 'w', encoding='UTF-8') as kor_f:
                kor_f.write("정산일시\t김치찌개 제육정식 생선정식 오늘수입 누적수입\n")
                self.total_income = self.today_income
                kor_f.write("%s\t%d\t%d\t%d\t%d\t%d\n"
                            % (today_date, self.get_menu[0], self.get_menu[1], self.get_menu[2], self.today_income, self.total_income))

                
    def check_customer_number(self):
        print("한식당 현재 현황...")
        time.sleep(1)
        print("현재 고객 현황 : 총 고객: %d 김치찌개: %d 제육정식: %d 생선정식: %d" % (sum(self.get_menu), self.get_menu[0], self.get_menu[1], self.get_menu[2]))
        time.sleep(1)
        print("오늘 매출 현황 : %d원" % self.today_income)
        delete_data = input("고객 현황을 모두 초기화 하시겠습니까? (y, n)").lower()
        if delete_data[0] == 'y':
            makesure = input("정말 초기화 하시겠습니까? (y, n)").lower()
            if makesure[0] == 'y':
                self.reset_number_served()

class WestRestaurant(Restaurant):

    def __init__(self, name):
        self.restaurant_name = name
        self.cuisine_type = '양식'
        self.today_customer = 0
        self.get_grade = ''
        self.today_income = 0
        self.total_income = 0

    def set_selection(self):
        self.today_customer += 1
        self.today_income = 0
        while True:
            custom_prefer = []
            set_select = input("1. A세트(20000원, 3접시)\n2. B세트(30000원, 4접시)\n세트를 선택하세요(1,2) >>>")
            if set_select == '1':
                self.today_income += 20000
                for i in range(0,3):
                    custom_prefer.append(random.randint(1, 3))
                return custom_prefer
            elif set_select == '2':
                self.today_income += 30000
                for i in range(0,4):
                    custom_prefer.append(random.randint(1, 3))
                return custom_prefer
            else:
                print("올바른 번호를 입력하십시오")
                
    def serving_customer(self, preference):
        custom_score = 0
        custom_grade = ['C', 'B', 'A', 'S', 'SS'] #이 부분이 긴가민가
        for i in range(0, len(preference)):
            served_dish = int(input("%d번째 요리: 어떤 것을 서빙하시겠습니까?\n1. 피자, 2. 스테이크, 3, 연어요리\n>>>" % (i+1)))
            if preference[i] == served_dish:
                custom_score += 1

        self.today_income += custom_score * 10000
        self.get_grade = custom_grade[custom_score]
        print("당신은 손님의 선호를 %d번 맞추었으므로 평점 %s를 받고 추가로 팁을 %d원 더 받았습니다." % (custom_score, custom_grade[custom_score], (custom_score * 10000)))

    def accounting_west(self, today_date):
        try:
            with open("양식고객일지.txt", 'r', encoding='UTF-8') as west_f:
                self.total_income = int(((west_f.readlines())[-1].split("\t"))[-1]) + self.today_income
            with open("양식고객일지.txt", 'a', encoding='UTF-8') as west_f:
                west_f.write("%s\t%s\t%d\t%d\n" % (today_date, self.get_grade, self.today_income, self.total_income))

        except:
            with open("양식고객일지.txt", 'w', encoding='UTF-8') as west_f:
                west_f.write("일시\t\t손님평점 오늘수입 누적수입\n")
                self.total_income = self.today_income
                west_f.write("%s\t%s\t%d\t%d\n" % (today_date, self.get_grade, self.today_income, self.total_income))


rest_type = int(input("어떤 레스토랑을 여시겠습니까? (1.한식, 2,양식)"))
rest_name = input("레스토랑 이름을 지어주세요.")
if rest_type == 1:
    opening_rest = KoreanRest(rest_name)
    opening_rest.describe_restaurant()
    while True:
        selection = input("1. 주문을 받는다.\n2. 가계 현황 & 초기화\n3. 정산 & 마무리\n입력>>>")
        if selection == '1':
            customer_order = []
            for i in range(0, len(opening_rest.KoreanMenu)):
                customer_order.append(random.randint(1, len(opening_rest.KoreanMenu)))
            menulist = list(opening_rest.KoreanMenu.keys())
            print("손님이 %d명 오셨습니다. (김치찌개: %d명, 제육정식: %d명, 생선정식: %d명)"
                  % (sum(customer_order), customer_order[0], customer_order[1], customer_order[2]))
            opening_rest.take_order(customer_order)

        elif selection == '2':
            opening_rest.check_customer_number()

        elif selection == '3':
            today_moment = time.strftime("%m/%d(%a)%H", time.localtime(time.time()))
            opening_rest.accounting_kor(today_moment)
            break
        else:
            print('올바른 명령을 입력하십시오')

elif rest_type == 2:
    opening_rest = WestRestaurant(rest_name)
    opening_rest.describe_restaurant()
    while True:
        opening_rest.check_customer_number()
        open_close = input("손님을 받으시겠습니까? (y, n)").lower()
        if open_close[0] == 'y':
            opening_rest.serving_customer(opening_rest.set_selection())
            at_moment = time.strftime("%m/%d(%a)%H", time.localtime(time.time()))
            opening_rest.accounting_west(at_moment)
        else:
            break
