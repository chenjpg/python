def normalize(name):
    return name[0].upper()+name[1:].lower() if name else name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)