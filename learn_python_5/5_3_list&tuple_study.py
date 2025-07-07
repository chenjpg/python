#List study
classmates = ['adam', 'bob', 'alex']
print (classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
#print(classmates[3])
#当索引超出了范围时
#Python会报一个IndexError错误，所以，要确保索引不要越界，
#记得最后一个元素的索引是len(classmates) - 1。
print(classmates[-1])
classmates.append('michael')
#末尾加入michael
print(classmates)
classmates.insert(1,'jack')
#指定位置插入jack
print(classmates)
classmates.pop()
#删除队尾元素
print(classmates)
classmates.pop(1)
#删除指定元素1是jack
print(classmates)
classmates[1]='sarah'
#替换第一个元素
print(classmates)
#list元素类型可以不同
L = ['apple', 123,True]
#list元素里面可以是另一个list
s = ['python', 'java',['asp','php'],'sheme']
print(len(s))
p=['asp','php']
s1=['python','java',p,'c']
#拿到php可以写p[1],s[2][1]
print(s1[2][1])
L1 = []
print(len(L1))

#Tuple study
#这样就创建了一个tuple
classmates = ('Michael', 'Bob', 'Tracy')
#无法更改append()，insert()
#不可变的tuple有什么意义？因为tuple不可变，
# 所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#当你定义一个tuple时
t= (1,2)
print(t)
#定义一个空的tuple
t=()
print(t)
t=(1)
#定义的不是tuple，是1这个数！
#这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
print(t)
t=(1,)
#这个才是一个tuple
print(t)
#Python在显示只有1个元素的tuple时，也会加一个逗号,
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)