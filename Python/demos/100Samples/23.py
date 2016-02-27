"""
2 【程序23】
 3 题目：打印出如下图案（菱形）
 4
 5    *
 6   ***
 7  *****
 8 *******
 9  *****
10   ***
11    *
"""

def main():
    for i in range(1, 8, 2):
        #python中字符串可以做乘法和加法
        print(' '*(4-(i+1)//2)+'*'*i)
    for i in range(5, 0, -2):
        print(' '*(4-(i+1)//2)+'*'*i)

if __name__=="__main__":
   main()

