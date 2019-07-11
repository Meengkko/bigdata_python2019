class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


    def print_number(self):
        print("first: %d, second: %d" %(self.first, self.second))


    def add(self):
        result = self.first + self.second
        return result


a = FourCal()
a.setdata(1, 2)
a.print_number()
print(a.add())
print("first: %d, second: %d" % (a.first, a.second))
print(a.first + a.second)

# 위와 같이 python의 모든 클래스의 멤버 변수, 함수는 속성이 public이라
# 외부에서 모두 접근이 가능하다.
# 하지만 클래스의 멤버 변수에 대해서 설정하는 것은
# 클래스 정의시 멤버변수 정의, 생성자, setXXX()함수로 정의 및 수정을 하는 것이
# 객체지향 프로그래밍에 가깝다.
# temp = [1,2,3,4]
# temp.__class__()
# 객체지향언어에서의 private 개념은 __멤버변수__.__멤버함수__()로
# 적용할 수 있다. 접근은 가능하지만 사용하지 않는 암묵적인 룰을 준수한다.