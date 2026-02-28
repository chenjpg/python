
L = ['Michael','Sarah','Tracy','Bob','Jack']
# 取前3个元素，应该怎么做？
# 老方法
print(L)
print([L[0],L[1],L[2]])

# 之所以是笨办法是因为扩展一下，取前N个元素就没辙了
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 对这种经常取指定索引范围的操作，
# 用循环十分繁琐，
# 因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
print(L[0:3])
# L[0:3]表示，从索引0开始取，直到索引3为止，
# 但不包括索引3。即索引0，1，2，正好是3个元素。
# 也可以从1开始
print(L[1:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，
# 那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])
L1 = list(range(100))
print(L1)
# 前十个
print(L1[:10])
# 后十个
print(L1[-10:])
# 前11-20
print(L1[11:20])
# 前10个数，每两个取一个：
print(L1[:10:2])
# 所有数，每5个取一个：
print(L1[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L1[:])
# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
T= tuple(range(100))
print(T[:3])
print(T[::5])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('abcdefg'[:3])
print('abcdefg'[::2])
print('abcdefg'[0:-2])