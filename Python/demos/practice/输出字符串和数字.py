#在javascript里我们会理想当然的将字符串和数字连接,因为是动态语言嘛.但在Python里有点诡异,如下:
#! /usr/bin/python

"""
a=2
b="test"
c=a+b
"""

#运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
#! /usr/bin/python
#运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
a=2
b="test"
c=str(a)+b
d="1111"
e=a+int(d)
#How to print multiply values
print ("c is %s,e is %i" % (c,e))

price = 12.34
s = "the price is " + str(price)
print(s)

age_str = "30s"
try:
    age = int(age_str)
except ValueError:
    print("age string has value error")
    age_str = "30"
    age = int(age_str)
print("the age is:%d"%age)


'''
知识点:
    * 用int和str函数将字符串和数字进行转换
    * 注释以#开头,而不是习惯的//
    * 打印多个参数的方式
    '''