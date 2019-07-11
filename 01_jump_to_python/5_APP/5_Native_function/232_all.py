# all은 iterable 객체 (2개 이상의 값을 담을 수 있는 자료형 튜플, 리스트, 딕셔너리)에 적용가능하다.

print(all([1, 2, 3]))     # True
print(all([1, 2, '']))    # False
print(all((1, 2)))
print(all((1, 0)))
print(all({"컵": "물", "바구니": "아두이노"}))
print(all({"": "", "바구니": "아두이노"}))
print(all({}))
print(all(list({}.values())))

result = [1,2,3].append(4)
print(result)
print([1,2,3].append(4))
result = [1,2,3]
result.append(4)
print(result)

print([1,2,3].count(2))