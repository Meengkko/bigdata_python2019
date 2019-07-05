negative = []
positive = []
numbers = input()
numList = numbers.split(" ")
for i in range(0, len(numList)):
    if int(numList[i]) >= 0:
        positive.append(int(numList[i]))
    else:
        negative.append(int(numList[i]))

print(negative + positive)