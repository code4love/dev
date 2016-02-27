#【程序37】
# 题目：对输入的n个数进行排序

l = []
s = input("input 10 numbers:")
for n in s.split():
    l.append(int(n))
l.sort()
print(l)
