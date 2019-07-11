class FourCal:

    def __init__(self, first, second):
        # self.first = first
        # self.second = second
        self.first = first
        if second == 0:
            print("두번째 값에는 0이 올 수 없습니다.")
            print("프로그램 강제 종료하겠습니다.")
            exit()
        self.second = second

    def print_number(self):
        print("first: %d, second: %d" %(self.first, self.second))


a = FourCal(1, 2)
a.print_number()
b = FourCal(3, 0)
b.print_number()
