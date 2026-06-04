import functools
num = int('123')
num1 = int('123',base=8)
num2 = int('123',16)
print(num,num1,num2)
def int2(x,base=2):
    return int(x,base)
print(int2('1000'))
print(int2('10000',base=10))
int2=functools.partial(int,base=2)
max2 = functools.partial(max,10)
print(max2(5,6,7))