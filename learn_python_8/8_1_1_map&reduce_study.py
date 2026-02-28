# python内建了map()和reduce()函数
# 我们先看map。map()函数接收两个参数，
# 一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
# 举例说明，比如我们有一个函数f(x)=x^2，要是吧这个函数作用在一个list [1,2,3,4,5,6,7,8,9]
# 就可以用map() 实现如下

from functools import reduce

def f(x):
    return x*x
r = map(f,range(10))
print(list(r))
# 把list所有数字转为字符串
print(list(map(str, [1,2,3,4,5,6,7,8,9])))
# 介绍reduce
# reduce(f,[x1,x2,x3,x4])= f(f(f(x1,x2),x3),x4)
# def add(a,b):
#     return a+b
# print(reduce(add, [1,2,3,4,5,6,7,8,9]))
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
print(str2int('10'))
print(str2int('1'))