while True:
    Width = int(input("홀수를 입력하세요 (0 <- 종료): "))
    if Width == 0:
        break
    elif Width % 2 == 0 or Width < 0:
        continue
    print(" " + "-" * Width)
    for i in range(1, Width + 1):
        print("|"+" " * (abs(Width - (2 * i - 1)) // 2) + "*" * (Width - abs(Width - (2 * i - 1)))+" " * (abs(Width - (2 * i - 1)) // 2) + "|")
    print(" " + "-" * Width)
