import random
import time

lottery = []

while len(lottery) != 6:
    lottery.append(random.randint(1, 45))
    lottery = list(set(lottery))

for key, value in enumerate(lottery):
    print("%d번 숫자" % (key+1), end=" ")
    time.sleep(1)
    print("%d입니다." % value)
    time.sleep(0.5)
