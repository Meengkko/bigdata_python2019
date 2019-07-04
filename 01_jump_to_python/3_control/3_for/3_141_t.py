total = 0

for i in range(10):
    print(i, end = " ")
    total = total + i

print("\ntotal: %d\n" % total)

total = 0
for i in range(1, 11):
    print(i, end = " ")
    total = total + i

print("\ntotal: %d\n" % total)

total = 0
for i in range(1, 11, 2):
    print(i, end = " ")
    total = total + i

print("\ntotal: %d" % total)
