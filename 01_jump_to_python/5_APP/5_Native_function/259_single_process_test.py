import time
from datetime import datetime

s_dt = datetime.now()
print(s_dt) # 타임스탬프 (로그 작성 또는 프로그램 성능 측정시 사용)

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

for i in range(5):
    long_task()

print("end")

e_dt = datetime.now()
print(e_dt)
print(e_dt - s_dt)
