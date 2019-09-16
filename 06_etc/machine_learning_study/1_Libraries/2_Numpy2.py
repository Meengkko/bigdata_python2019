import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])

# 행렬의 dot product를 numpy에서 구현할 수 있다.
C = np.dot(A, B)
print(C)

# numpy broadcast 크기가 다른 두 행렬의 사칙연산을 가능하게 한다.
# 그러나 행렬 곱에는 적용되지 않는다.
print(A + 1)

# 전치행렬 구하기
print(A.T)

D = np.array([10, 20, 30, 40, 50, 60]).reshape(3, 2)

# 슬라이싱
print("D\n", D)
print("D.shape ==", D.shape)
print("D[0:-1, 1:2] ==", D[0:-1, 1:2])
print("D[:, 0] ==", D[:, 0])

# 행렬 iterator

E = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

print("E\n", E, "\n")
print("E.shape", E.shape, "\n")

it = np.nditer(E, flags=['multi_index'], op_flags=['readwrite'])

# iterator는 while문과 주로 같이 쓰인다.

while not it.finished:
    idx = it.multi_index
    print("current value => ", E[idx])
    it.iternext()
