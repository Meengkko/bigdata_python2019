# coding: cp949

service = """
   \\
  ( \\   ( (
  )  \\  ) )
==============
 \          /==
  \ coffee /   |
   \  ♡  / ===
  ==========
"""

coffee = 10
money = 0
coffee_price = 300

while True:
    
    money = int(input("돈을 넣어 주세요: "))
    if money >= coffee_price:
        if money > coffee_price:
            print("거스름돈 %d를 드리고, " % (money - coffee_price), end = "")
        print("커피를 드립니다.")
        print(service)
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    
    print("남은 커피의 양은 %d개 입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
