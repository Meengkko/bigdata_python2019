import numpy as np

A = np.array([[10, 20, 30], [40, 50, 60]])
print(A.shape)

row_add = np.array([70, 80, 90]).reshape(1, 3)
column_add = np.array([1000, 2000]).reshape(2, 1)

# numpy, concatenate 에서 axis = 0 행(row) 기준
# A 행렬에 row_add 행렬 추가
B = np.concatenate((A, row_add), axis=0)
print(B)

# numpy, concatenate 에서 axis = 1 열(column) 기준
# B 행렬에 column_add 행렬 추가
C = np.concatenate((A, column_add), axis=1)
print(C)

random_number1 = np.random.rand(3)
random_number2 = np.random.rand(1, 3)
random_number3 = np.random.rand(3, 1)

print(random_number1, "\n", random_number2, "\n", random_number3, "\n")

X = np.array([2, 4, 6, 8])
print("np.sum(X) ==", np.sum(X))
print("np.exp(X) ==", np.exp(X))
print("np.log(X) ==", np.log(X), "\n")

# max, min, argmax, argmin
print("np.max(X) ==", np.max(X))
print("np.min(X) ==", np.min(X))
print("np.argmax(X) ==", np.argmax(X))
print("np.argmin(X) ==", np.argmin(X))

# ones, zeros
D = np.ones([3, 3])
print("D.shape ==", D.shape, "\nD ==", D)
E = np.zeros([3, 2])
print("E.shape ==", E.shape, "\nE ==", E)

Y = np.array([[2, 4, 6], [1, 2, 3], [0, 5, 8]])

print("np.max(Y) ==", np.max(Y, axis=0))  # axis=0 열기준
print("np.min(Y) ==", np.min(Y, axis=0))  # axis=0 열기준

print("np.max(Y) ==", np.max(Y, axis=1))  # axis=1 행기준
print("np.min(Y) ==", np.min(Y, axis=1))  # axis=1 행기준

print("np.argmax(Y) ==", np.argmax(Y, axis=0))  # axis=0 열기준
print("np.argmin(Y) ==", np.argmin(Y, axis=0))  # axis=0 열기준

print("np.argmax(Y) ==", np.argmax(Y, axis=1))  # axis=1 행기준
print("np.argmin(Y) ==", np.argmin(Y, axis=1))  # axis=1 행기준

