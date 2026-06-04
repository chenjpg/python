import numpy as np

# 定义一个矩阵
A = np.array([[1, -1,0], [1,0,-1],[-6,2,3]])

# 计算矩阵的逆
A_inv = np.linalg.inv(A)

print("矩阵 A 的逆矩阵是：")
print(A_inv)