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


# Bài tập buổi 3:
# ex_1
A_ex1 = np.array([[2, 1],
                [0, 3]])
B_ex1 = np.array([[1, 0],
                [2, 1]])
print("A_ex1 @ B_ex1 =\n", A_ex1 @ B_ex1)  
print("B_ex1 @ A_ex1 =\n", B_ex1 @ A_ex1)  


A2 = np.array([[1,2],[0,1]])
B3 = np.array([[3,0],[1,2]])
print("Bài luyện 1:", A2 @ B3)

C2 = np.array([[2,-1],[3,0]])
D3 = np.array([[1,4],[-2,1]])
print("Bài luyện 2:", C2 @ D3)