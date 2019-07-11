import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %p %I:%M:%S sec', time.localtime(time.time())))

# print(list(time.localtime(time.time())))
