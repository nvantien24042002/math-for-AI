import numpy as np
print("=== Ma trận và phép biến đổi ===\n")
# Bài 1 : Scaling Matrix
A_scale = np.array([[2,0],
                    [0,2]])
v = np.array([3,1])
print("Bài 1 : Scaling: A @ v = ",A_scale @ v)
# Bài 2 : Rotation 90 deg
A_rot = np.array([[0,-1],
                    [1,0]])
v2 = np.array([1,0])
print("Bài 2: Rotation: A @ v = ",A_rot @ v)
# Bài 3 : Reflection qua trục x 
A_reflect = np.array([[1,0],[0,-1]])
v3 = np.array([4,5])
print("Bài 3 : Reflection: A @ v =", A_reflect @ v3)