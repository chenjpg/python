def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)  # 将盘子从源柱子移动到目标柱子
    else:
        move(n - 1, a, c, b)  # 将 n-1 个盘子从 A 移动到 B，借助 C
        print(a, '-->', c)      # 将第 n 个盘子从 A 移动到 C
        move(n - 1, b, a, c)  # 将 n-1 个盘子从 B 移动到 C，借助 A

# 调用函数，移动 3 个盘子
move(3, 'A', 'B', 'C')