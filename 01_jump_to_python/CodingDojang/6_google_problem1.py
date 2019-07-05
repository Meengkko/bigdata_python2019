N = 10001
counter = 0

for i in range(1, N):
    numStr = str(i)
    for j in range(len(numStr)):
        if numStr[j] == '8':
            counter += 1

print(counter)