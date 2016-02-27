#【程序29】
#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def func(n):
    a = 0
    while (n>0):
        a += 1
        print(n%10, end="")
        n //= 10
    print("\n", a)

def main():
    while True:
        n = int(input("input an integer:"))
        if (n==0):
            break
        func(n)

if (__name__=="__main__"):
    main()

