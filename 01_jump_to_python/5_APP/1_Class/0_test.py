class Cookie:
    # def __init__(self):
    #     pass
    def __init__(self):
        print("생성자 호출")
    def eat(self):
        print("아 맛있다~")


print("Debug1")
a = Cookie()
a.eat()
print("Debug2")