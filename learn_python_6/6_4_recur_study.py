from fact import fact_iter


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(5))
# 如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
#
# => fact(5)
# => 5 * fact(4)
# => 5 * (4 * fact(3))
# => 5 * (4 * (3 * fact(2)))
# => 5 * (4 * (3 * (2 * fact(1))))
# => 5 * (4 * (3 * (2 * 1)))
# => 5 * (4 * (3 * 2))
# => 5 * (4 * 6)
# => 5 * 24
# => 120
# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
# 栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# print(fact(1000))
# 解决递归调用栈溢出的方法是通过尾递归优化，
# 事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，
# 并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
print(fact_iter(5,1))
print(fact(5))
# 可以看到，return fact_iter(num - 1, num * product)
# 仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    print("fact_iter : %s, %s" %(num,product))
    if num ==1:
        return product
    return fact_iter (num-1,num*product)

print(fact(10))