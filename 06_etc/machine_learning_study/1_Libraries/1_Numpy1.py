import numpy as np

A = np.array([[1, 0], [0, 1]])
B = np.array([[1, 1], [1, 1]])

print(A + B)

C = np.array([1, 2, 3])
D = np.array([4, 5, 6])

print("C ==", C, "D ==", D)
print("C.shape ==", C.shape, "D.shape ==", D.shape)
print("C.ndim ==", C.ndim, "D.ndim ==", D.ndim)

print("C + D ==", C+D)
print("C - D ==", C-D)
print("C * D ==", C*D)
print("C / D ==", C/D)

E = np.array([[1, 2, 3], [4, 5, 6]])
print(E.reshape(3, 2))
