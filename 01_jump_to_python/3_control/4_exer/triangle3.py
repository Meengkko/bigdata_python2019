while True:
    Width = int(input("홀수를 입력하세요 (0 <- 종료): "))
    if Width == 0:
        break
    elif Width % 2 == 0 or Width < 0:
        continue
    print(" "+"-"*Width)
    for i in range(1, Width+1, 2):
        print("|"+" "*((Width//2)-(i//2))+"*"*i+" "*((Width//2)-(i//2))+"|")
    for i in range(1, Width-1, 2):
        print("|"+" "*((i+1)//2)+"*"*(Width - i - 1)+" "*((i+1)//2)+"|")
    print(" "+"-"*Width)

