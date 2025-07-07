def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-99))

#空函数
def nop():
    pass
# pass语句什么都不做，那有什么用？
# 实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# if age >= 18:
# 	pass
#参数检查
# my_abs(1,2)
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# Traceback (most recent call last):
#   File "/Users/zhuoqichen/Desktop/code/python/learn_python_6/6_2_deffunc_study.py", line 17, in <module>
#     my_abs(1,2)
# TypeError: my_abs() takes 1 positional argument but 2 were given

# 但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别
# my_abs('A')
# Traceback (most recent call last):
#   File "/Users/zhuoqichen/Desktop/code/python/learn_python_6/6_2_deffunc_study.py", line 23, in <module>
#     my_abs('A')
#   File "/Users/zhuoqichen/Desktop/code/python/learn_python_6/6_2_deffunc_study.py", line 2, in my_abs
#     if x>=0:
#        ^^^^
# TypeError: '>=' not supported between instances of 'str' and 'int'
# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad open type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-99))

my_abs('a')
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：
#     raise TypeError('bad open type')
# TypeError: bad open type

#返回多个值
import math
def move(x,y, step, angle=0):
	nx = x+step*math.cos(angle)
	ny= y-step+math.sin(angle)
	return nx,ny

