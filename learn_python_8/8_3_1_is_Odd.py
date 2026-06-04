def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
# 也可以使用 lambda 匿名函数来实现同样的功能
list(filter(lambda n: n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]