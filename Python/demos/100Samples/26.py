#【程序26】
#题目：利用递归方法求5!。

def factorial(n):
    if n==1 or n==2:
        return n
    else:
        return n*factorial(n-1)

print(factorial(10))