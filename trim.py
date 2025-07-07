def trim(s):
    # 处理空字符串的特殊情况
    if not s:
        return s
    
    # 去除左侧空格
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    
    # 去除右侧空格
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')