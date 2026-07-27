import numpy as np
print("=== Bài 1: Vector cơ bản ====\n")
# Bài 1: Tính độ dài vector v = (6, 8)
v1 = np.array([6,8])
print("Bài 1 : v =", v1)
print("Bài 1 : |v| =", np.linalg.norm(v1))
print()
# Bài 2: Nhân vô hướng v = (5, -2), tính 3v
v2 = np.array([5,-2])
print("Bài 2 : v =", v2)
print("Bài 2 : 3v =", 3 * v2)
print()
# Bài 3: Cộng vector a=(1,4), b=(3,-1)
a = np.array([1, 4])
b = np.array([3, -1])
sum_ab = a + b
print("Bài 3 : a =", a, ", b =", b)
print("Bài 3 : a+b =", sum_ab)
print("Bài 3 : |a+b| =", np.linalg.norm(sum_ab))

