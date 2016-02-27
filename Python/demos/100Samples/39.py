#【程序39】
#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

s = [1, 3, 4, 8, 30, 40, 90]
#s = [10, 8, 6]
n = int(input("input an integer:"))
for i in range(0, len(s)-1):
    if ((n>s[i] and n<s[i+1]) or (n<s[i] and n>s[i+1])):
        s.insert(i+1, n)
        break

s.reverse()
print(s)