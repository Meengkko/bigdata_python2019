class Restaurant:
    def __init__(self, name, types):
        self.restaurant_name = name
        self.cuisine_type = types

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다." % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)

    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.restaurant_name)


opening_rest = []
for i in range(0, 3):
    rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split(" ")
    opening_rest.append(Restaurant(rest_name, rest_type))
    opening_rest[i].describe_restaurant()
    opening_rest[i].open_restaurant()
    if i == 2:
        print("\n저녁 10시가 되었습니다.\n")

for i in range(0, 3):
    del opening_rest[0]
