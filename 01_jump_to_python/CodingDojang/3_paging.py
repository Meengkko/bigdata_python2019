m = int(input("총 건수: "))
n = int(input("한 페이지에 들어가는 게시물 수: "))
page_counter = [m // n, 1 if m % n else 0]
print("필요한 홈페이지 개수 : %d " % sum(page_counter))
