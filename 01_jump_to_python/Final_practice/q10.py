class Calculator:
    def __init__(self, input_list):
        self.num_list = input_list

    def sum(self):
        return sum(self.num_list)

    def avg(self):
        return sum(self.num_list)/len(self.num_list)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
