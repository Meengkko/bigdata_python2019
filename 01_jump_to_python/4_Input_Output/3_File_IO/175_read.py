f = open("새파일.txt", 'r', encoding='UTF-8')
data = f.read()
print(data, end="")

f.close()