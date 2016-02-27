#题目：判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt
for n in range(101, 201):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            break
    else:
        print("%-5d"%(n), end="")
