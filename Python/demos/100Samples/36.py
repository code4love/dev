#【程序36】【筛选法】
#题目：求100之内的素数　　　

def main():
    """输出100以内所有素数"""
    for n in range(2, 100):
        for i in range(2, n//2+1):
            if (n%i==0):
                break
        else:
            print(n, end=" ")


if (__name__=="__main__"):
    main()