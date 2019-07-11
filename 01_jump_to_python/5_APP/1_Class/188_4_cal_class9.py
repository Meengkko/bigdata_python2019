class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def print_number(self):
        print("first: %d, second: %d" %(self.first, self.second))

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
# parent class
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

    def div(self):  # 메서드 오버라이딩 : 자식 클래스에서 부모 클래스의 멤버 함수를 재정의
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
# child class

child = MoreFourCal(4, 0)
print(child.div())

parent = FourCal(4, 0)
print(parent.div())


