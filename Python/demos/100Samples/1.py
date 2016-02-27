#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        if j==i:
            continue
        for k in range(1, 5):
            if k==i or k==j:
                continue
            print(i*100+j*10+k, end=" ")
            count += 1
print()
print(count)