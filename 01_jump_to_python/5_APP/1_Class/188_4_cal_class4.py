class FourCal:
# first = 0
# second = 0 # 중간에 멤버 변수를 정의할 수 있어도 명시적으로 클래스
             # 멤버 변수를 class 다음에 지정하는 것은
             # 프로그램 유지보수와 가독성에 더 좋다고 볼 수 있다.
    def setdata(self, first, second):
        self.first = first # 멤버 변수가 없음에도 중간에 새로운 객체생성 이후에
                           # 클래스의 멤버변수를 생성하는 것이 가능하다.
        self.second = second


    def print_number(self):
        print("first: %d, second: %d" %(self.first, self.second))


a = FourCal()
a.setdata(1, 2)
a.print_number()
print(id(a))
print(id(a.first))

b = FourCal()
b.setdata(3, 4)
b.print_number()
print(id(b))
print(id(b.first))
