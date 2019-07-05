while True:
    Width = int(input("홀수를 입력하세요 (0 <- 종료): "))
    if Width == 0:
        break
    elif Width % 2 == 0 or Width < 0:
        continue
    for i in range(1, Width+1, 2):
        print(" "*((Width//2)-(i//2))+"*"*i)