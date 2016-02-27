#【程序30】
#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def func(s):
    flag = True
    for i in range(0, (len(s)+1)//2):
        if (s[i]!=s[len(s)-1-i]):
            flag = False
            break
    if(flag):
        print("yes")
    else:
        print("no")

def main():
    while True:
        n = int(input("input an integer:"))
        if (n==0):
            break
        func(str(n))

if (__name__=="__main__"):
    main()