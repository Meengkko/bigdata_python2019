class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(1))
print(cal1.add(2))
print(cal2.add(3))
print(cal2.add(4))
print(cal3.add(5))
print(cal3.add(6))