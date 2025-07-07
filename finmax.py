def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        mini = L[0]
        maxi = L[0]
        for i in L:
            if i < mini:
                mini = i
            if i > maxi:
                maxi = i 
        return (mini, maxi)
        

            
            




# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')