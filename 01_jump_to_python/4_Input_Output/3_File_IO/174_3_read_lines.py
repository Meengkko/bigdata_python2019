f = open("새파일.txt", 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line, end="")

f.close()