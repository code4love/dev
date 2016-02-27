#题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
from math import sqrt
def main():
    for n in range(1, 1001):
        sum = n*-1
        k = int(sqrt(n))
        for i in range(1,k+1):
            if n%i == 0:
                sum += n/i
                sum += i
        if sum == n:
            print(n, end=" ")

if __name__=="__main__":
    main()
