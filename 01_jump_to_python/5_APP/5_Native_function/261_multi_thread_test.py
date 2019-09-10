import time
import threading
from datetime import datetime


def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)


s_dt = datetime.now()
print(s_dt)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("end")

e_dt = datetime.now()
print(e_dt)
print(e_dt - s_dt)