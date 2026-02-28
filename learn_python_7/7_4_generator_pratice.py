def triangles():
    prelist=[1]
    while True:
        yield prelist
        templist = [1]
        for i in range(1,len(prelist)):
            templist.append(prelist[i-1]+prelist[i])
        templist.append(1)
        prelist=templist
        # l = [1]
        # while True:
        #     yield l
        #     l = [1] + [x + y for i, x in enumerate(l[:-1]) for j, y in enumerate(l[1:]) if i == j] + [1]



# 期待输出:
         # [1]
        # [1, 1]
       # [1, 2, 1]
      # [1, 3, 3, 1]
     # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
   # [1, 6, 15, 20, 15, 6, 1]
  # [1, 7, 21, 35, 35, 21, 7, 1]
 # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t,o in zip(results,range(n,0,-1)):
    print(' '*o+str(t))

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
