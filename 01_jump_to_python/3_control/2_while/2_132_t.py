# coding: cp949

menu_prompt = """1. 입력
2. 조회
3. 수정
4. 삭제
5. 종료
메뉴를 선택하세요 (1~5): """

customer_choice = 0
while True:
    customer_choice = int(input(menu_prompt))

    # 아래와 같은 구조는 C에서 switch/case로 하는 것이 더 효율적이나 파이썬에서는 switch/case를 지원하지 않는다.

    if customer_choice == 1:
        pass
    elif customer_choice == 2:
        pass
    elif customer_choice == 3:
        pass
    elif customer_choice == 4:
        pass
    elif customer_choice == 5:
        break
    else:
        print("1~5의 숫자만 유효합니다.")
