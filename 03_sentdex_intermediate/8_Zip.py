x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a, b, c in zip(x, y, z):
    print(a, b, c)

print(zip(x, y, z))

# [print(i) for i in zip(x, y, z)]

# [print(x, y) for x, y in zip(x, y)]
# print(x)

[print(a, b) for a, b in zip(x, y)]
print(a)
