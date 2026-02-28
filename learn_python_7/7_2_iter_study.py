# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）
# list这种数据类型虽然有下标，
# 但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，
# 都可以迭代，比如dict就可以迭代：

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
# 因为dict的存储不是按照list的方式顺序排列，
# 所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。
# 如果要迭代value，
# 可以用for value in d.values()，
for value in d.values():
    print(value)
# 如果要同时迭代key和value，
# 可以用for k, v in d.items()。
for k,v in d.items():
    print(k,v)
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABCD':
    print(ch)
# 所以当我们使用for循环时，只要作用于一个可迭代的对象，
# for循环就可以正常运行，而我们不太关心该对象究竟是List还是其他数据类型
# 那么如何判断一个对象时可迭代对象呢？方法时通过collections.abs模块的Iterable类型判断
from collections.abc import Iterable
print(isinstance('abc', Iterable)) # str是否是可迭代
print(isinstance([1,2,3], Iterable)) # list是否可以迭代
print(isinstance(123, Iterable)) #整数可不可以迭代
# 最后一个小问题。如果要对list实现java那样的的下标循环怎么办
# python内置的enumerate 函数可以把一个list变成索引元素对
# 这样就可以在for 循环中同时迭代索引和元素本身
for i, value in enumerate(['A','B','C']):
    print(i, value)
# 在上面的for循环中，同时引用了两个变量，在python中是很常见的
# 比如一下代码
for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)