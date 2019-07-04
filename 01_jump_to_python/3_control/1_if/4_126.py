# coding: cp949

# pocket = ['종이','핸드폰', '현금']
pocket = ['종이','핸드폰','신용카드']

"""
if '현금' in pocket:
    print("택시를 타고 가라")
elif '신용카드' or '현금' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가세요")
"""

# if '현금' or '신용카드' in pocket:
# '현금'은 상수형 문자열 객체로서 값이 있기 때문에 무조건 True를 반환한다. 따라서 pocket에 현금과 신용카드가 있는 조건을 표현하려면 아래와 같이 작성해야 한다. 이는 프로그램 중복으로 볼 수는 없다.

if '현금' in pocket or '신용카드' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
