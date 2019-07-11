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

    def pow(self):
        result = self.first ** self.second
        return result


a = FourCal(4, 2)
b = FourCal(3, 8)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

a.setdata(9, 4)
b.setdata(382, 48)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

print(a.pow())