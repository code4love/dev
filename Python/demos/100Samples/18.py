#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def main():
    a = int(input("input an integer:"))
    count = int(input("input the count:"))
    b = a
    sum = 0
    while count>0:
        sum += a
        a = a*10 + b
        count -= 1
    print(sum)

if __name__ == "__main__":
    for i in range(2, 3):
        print(i)
    main()

