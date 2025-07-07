from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    def char2num(s):
        return DIGITS[s]
    
    for i in range (len(s)):
        if s[i] == '.':
            a = s[:i]
            b = s[i+1:]
            b = b[::-1]
            break

    def fnpos(x, y):
        return x * 10 + y
    def fnneg(x,y):
        return x/10+y
    
    m = reduce(fnpos,map(char2num,a))
    n = reduce(fnneg,map(char2num,b))/10


    return m+n




    

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')