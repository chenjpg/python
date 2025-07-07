# name = ['Michael','Bob','Tracy'] 
# scores = [95,75,65]
#耗时长
d = {'Michale':95,'Bob':75,'Tracy':65}
print (d['Michale'])
# 给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，
# 也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
# 可以猜到，这种key-value存储方式，在放进去的时候，
# 必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
d['Adam']=67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d["Adam"]=88
print(d["Adam"])
# 如果key不存在，dict就会报错：
#d['Thomas']
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas',-1))
print(d.pop('Bob'))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：

#     查找和插入的速度极快，不会随着key的增加而变慢；
#     需要占用大量的内存，内存浪费多。
# 而list相反：

#     查找和插入的时间随着元素的增加而增加；
#     占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# key = [1,2,3]
# d[key]='a list'
#dict 原本样子d ={a:1,b:2,c:3}
#调用.get() 调用key d["a"]
#set

s ={1,2,3}
print(s)
# 或者提供一个list作为输入集合：
s = set([4,5,6])
print(s)
#重复的元素在set中会被过滤
s  = {1,1,1,2,2,3,3}
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合
s1 = {1,2,3}
s2 = {2,3,4}
print(s1&s2)
print(s1|s2)
# 无法判断两个可变对象是否相等

#再议不可变对象
# str是不变对象，而list是可变对象
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
a.sort()
print(a)
# 对于不可变对象
a1 = 'abc'
print(a1.replace('a','A'))
print(a1)
#这种变了好像又没有变
#应该这样
a = 'abc'
b = a.replace('a','A')
print(b)
# replace方法创建了一个新字符串'Abc'并返回，
# 如果我们用变量b指向该新字符串，就容易理解了，
# 变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
