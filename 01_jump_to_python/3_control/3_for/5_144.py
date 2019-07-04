# coding: cp949

a = [1,2,3,4]
result = []

# Case 1
for num in a:
    result.append(num*3)
print(result)

# Case 2
result2 = [num * 3 for num in a]
print(result2)

# Case 3
result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)
