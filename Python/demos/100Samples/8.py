#题目：输出9*9口诀。
for i in range(1, 10):
    for j in range(1, 10):
       print(i, " * ", j, " = ", i*j, sep='')
    print()