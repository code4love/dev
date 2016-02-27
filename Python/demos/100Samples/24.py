#【程序24】
#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def main():
    a = 2
    b = 1
    s = a / b
    for i in range(1, 20):
        a = a + b
        b = a - b
        s += a / b
    print("%f"%s)

if __name__=="__main__":
    main()



