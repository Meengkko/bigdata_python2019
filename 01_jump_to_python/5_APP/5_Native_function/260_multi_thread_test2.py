import time
import threading
from datetime import datetime


def long_task(thread_number):
    for i in range(5):
        time.sleep(1)
        print(f"#{thread_number}thread working: {i+1}\n")


s_dt = datetime.now()
print(s_dt)

print("Start")
threads = []

for i in range(5):
    # 쓰레드의 인자를 넘기려면 args=() <= 튜플 형태로 넘긴다.
    t = threading.Thread(target=long_task, args=(i+1,))
    threads.append(t)

for t in threads:
    t.start()

print("end")

e_dt = datetime.now()
print(e_dt)
print(e_dt - s_dt)
