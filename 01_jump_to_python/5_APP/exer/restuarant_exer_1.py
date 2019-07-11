class Restaurant:
    def __init__(self, name, types):
        self.restaurant_name = name
        self.cuisine_type = types

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다." % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)


rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분):").split(" ")
opening_rest = Restaurant(rest_name, rest_type)
opening_rest.describe_restaurant()
opening_rest.open_restaurant()
