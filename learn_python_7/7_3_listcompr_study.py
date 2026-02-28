# 列表生成式List Comprehensions 是python 内置的非常强大的可以用来创建list的生成式
list(range(1,100))
print(list(range(1,100)))
L=[]
for i in range(1,100):
    L.append(i*i)
print(L)
# 但是循环太繁琐了，而列表生成式则可以用一行语句代替循环生成上面的list
print([x*x for x in range(1,100)])
# 写列表生成式时，把要生成的元素x*x放在前面，后面跟着for循环，就可以把list创造出来
# for循环加上判断这样我可以筛选出偶数的平方
print([x*x for x in range(1,100) if x%2 ==0])
# 还可以两层循环string
print([m+n for m in 'abc' for n in 'xyz'])
# 运用列表生成式，可以写出非常简洁的代码
# 例如下辖当前目录下所有文件的目录名可以通过一行代码实现
import os
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录
# for循环其实也可以同时使用两个或者多个变量
# 比如dict 的 items（）可以同时迭代key 和value
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,v)
# 因此列表生成式也可以使用两个变量来生成list
d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])
# 最后把一个list中的所有字符串变成小写
L1 = ['Hello','World','IBM','Apple']
print([s.lower() for s in L1])
# 但是我们不能够在if加上else
# [x for x in range(1,11) if x%2== 0 else 0]
# 这是因为跟在for后面加上if 是个筛选的条件，不能带else 否则如何筛选
# 另外一些同学发现把if 写在for 前面必须加上else 否则就会报错
print([x if x%2==0 else -x for x in L])
# 这是因为for前面部分是一个表达式，他必须根据x计算出一个结果。因此参考表达式：x if x%2 ==0,它无法根据x 计算出结果是因为缺少  else必须加上else
