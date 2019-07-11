class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value + val < 100:
            self.value += val
        else:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(10)
print(cal.value)
cal.add(20)
print(cal.value)
cal.add(30)
print(cal.value)
cal.add(60)
print(cal.value)
