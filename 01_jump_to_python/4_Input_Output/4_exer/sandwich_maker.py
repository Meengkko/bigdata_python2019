opening_message = """안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.
1. 주문
2. 종료"""
def input_ingredient():
    ingredient_list = []
    while True:
        selection = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if selection != "종료":
            ingredient_list.append(selection)
        else:
            break
    return ingredient_list

def make_sandwiched(ingredient_list):
    print("\n샌드위치를 만들겠습니다.")
    while ingredient_list:
        print("%s를 추가합니다." % ingredient_list.pop(0))
    return

print(opening_message)
orderOrGo = int(input("입력: "))
if orderOrGo == 1:
    ordered_topping = input_ingredient()
    make_sandwiched(ordered_topping)
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")