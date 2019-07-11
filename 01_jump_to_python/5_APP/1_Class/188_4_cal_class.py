class FourCal:
    first = 0
    second = 0
    pass

    def print_number(self):
        print("first: %d, second: %d" %(self.first, self.second))
        # self를 사용하지 않으면 멤버함수에서 사용하는 지역변수로 인식한다.
        # 따라서 아래 코드는 빌드리 에러를 발생하게 된다.
        # print("first: %d, second: %d" %(first, second))


a = FourCal()
a.print_number()