a = "Life is too short"
print(a.find('t'))
print(a.index('t'))

print("Debug 1")
print(a.find('k')) # 'k'가 없어도 프로그램 진행

print("Debug 2")
print(a.index('k')) # 'k'가 없으면 프로그램 종료(Runtime Error 발생)

print("Debug 3")
