

def power(x):
    return x*x
print(power(3))
# 这个时候，默认参数就排上用场了。
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x,y=2):
    s = 1
    while y > 0:
        y= y-1
        s = s*x
    return s

print(power(3,4))
print(power(3))

def enroll(name,gender):
    print('name: ', name)
    print('gender: ', gender)

enroll("Adam","Man")
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。

def enroll(name,gender,city="Beijing",age =6):
    print('name: ', name)
    print('gender: ', gender)
    print('city: ', city)
    print('age: ', age)

enroll("Adam","Man")
# 只有与默认参数不符的学生才需要提供额外的信息：
enroll("Adam","M",city="Tianjin")

def add_end(L=[]):
    L.append("end")
    return L
print(add_end([1,2,3]))

print(add_end())
print(add_end())
print(add_end())
# ['end']
# ['end', 'end']
# ['end', 'end', 'end']

#这就不对了
#所以默认参数必须是不变对象
def add_end(L=None):
    if L is None:
        L =[]
    L.append("end")
    return L
print(add_end())
print(add_end())
print(add_end())
# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，
# 多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc([1,2,3]))
print(calc([1,2,3,5,7,11,13,17,19,23,29]))
#可以写成这样
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc2(1,2,3,5,7,11,13,17,19,23,29))
print(calc2(1,2,3,5,7))
#如果已经有了一个list 后者tuple那该怎么办
nums = [1,2,3]
print(calc2(nums[0],nums[1],nums[2]))
#或者
# 所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc2(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数
def person(name,age,**kw):
    print('name: ', name, 'age: ', age,'other: ', kw)



person('Adam ',25)
person('Adam',25,city='Beijing')
person('Adam',25,city='Tianjin',job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra={'city':'Beijing','job':'Engineer'}
person('jack',24,**extra)
person('jack',24,city=extra['city'],job=extra['job'])
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。

#明明关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查
def person(name,age,**kw):
    if'city' in kw:
        pass
    if'job' in kw:
        pass
    print('name: ', name, 'age: ', age,'other: ', kw)
# 但是调用者仍可以传入不受限制的关键字参数：
person('jack',24,city='Beijing',job='Engineer',addr='chaoyang',zipcode='123456')
# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person('jack',24,'Beijing','Engineer')
# 由于调用时缺少参数名city和job，Python解释器把前两个参数视为位置参数，
# 后两个参数传给*args，但缺少命名关键字参数导致报错。
# 命名关键字参数可以有缺省值，从而简化调用：
person('jack',24,job='Engineer')
# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass

#参数组合
# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 必选参数（PositionalArguments）
# 必选参数是函数定义中没有默认值的参数。
# 调用函数时，必须按顺序传递这些参数。
# 示例：a和b在f1和f2中都是必选参数。
#
# 默认参数（Default Arguments）
# 默认参数是函数定义中已经赋予默认值的参数。
# 调用函数时，可以不传递这些参数，此时会使用默认值。
# 示例：c = 0
# 在f1和f2中是默认参数。
#
# 可变参数（args）
# 可变参数允许传递任意数量的位置参数。
# 这些参数会被收集到一个元组中。
# 示例：*args
# 在f1中是一个可变参数。
#
# 关键字参数（kwargs）
# 关键字参数允许传递任意数量的键值对参数。
# 这些参数会被收集到一个字典中。
# 示例： ** kw
# 在f1和f2中是关键字参数。
#
# 命名关键字参数（Keyword - Only Arguments）
# 命名关键字参数必须通过参数名显式传递。
# 它们不能通过位置传递。
# 命名关键字参数必须在可变参数之后定义。
# 示例：d 在f2中是命名关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,args=('a','b'),kw={})
f1(1,2,3,args=('a','b'),kw={'x':99})
f2(1,2,d=99,kw={'ext':None})

#最神奇的是你能够通过一个tuple 和dict你也可以调用上述函数：
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':99,'x':'#'}
f2(*args,**kw)

