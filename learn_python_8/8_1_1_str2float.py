from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(char):
    return DIGITS[char]
def str2float(s):
    Parts = s.split('.')
    intPart = reduce(lambda x,y: 10*x+y,map(char2num,Parts[0]))
    decimalPart = reduce(lambda x,y:(x+y)/10,map(char2num, Parts[1][::-1]),0)
    return intPart + decimalPart
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
