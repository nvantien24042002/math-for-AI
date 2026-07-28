import numpy as np

print("=== Bài 3: Nhân ma trận với ma trận ===\n")

A = np.array([[1, 2],
                [3, 4]])
B = np.array([[5, 6],
                [7, 8]])

print("A @ B =\n", A @ B)  
print("B @ A =\n", B @ A)

# Kết hợp xoay + phóng to
R = np.array([[0, -1],
                [1, 0]])
S = np.array([[2, 0],
                [0, 2]])

combined = S @ R
print("\nS @ R (xoay rồi phóng to) =\n", combined)

# Áp dụng lên vector v = (1, 0)
v = np.array([1, 0])
print("\nKết quả áp dụng lên v=(1,0):", combined @ v)