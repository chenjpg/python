import numpy as np

# 数据点
x = np.array([-2, -1, 0, 1, 2])  # x 坐标
y = np.array([3, 5, 1, 4, 10])  # y 坐标

# 拟合一个多项式
deg = 4  # 多项式的次数
coefficients = np.polyfit(x, y, deg)

# 打印多项式系数
print("多项式系数（从最高次到常数项）：", coefficients)

# 构造多项式函数
polynomial = np.poly1d(coefficients)

# 打印多项式
print("多项式：")
print(polynomial)

