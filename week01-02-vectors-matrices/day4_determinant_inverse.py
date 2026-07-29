# Identity Matrix : Ma trận đơn vị
import numpy as np
I = np.eye(2)
print(I)
# Determinant : định thức
A = np.array([[3, 0], [0, 2]])
print(np.linalg.det(A))
# Inverse Matrix
A = np.array([[2, 0], [0, 2]])
A_inv = np.linalg.inv(A)
print(A_inv)
print(A @ A_inv)
# Exercise 4 :

B = np.array([[4,2],[1,3]])
B_det = np.linalg.det(B)
print(B_det)