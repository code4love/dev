#! /usr/bin/python
#条件和循环语句

x=int(input("Please enter an integer:"))
if x<0:
    x=0
    print ("Negative changed to zero")
elif x==0:
    print ("Zero")
else:
    print ("More")

# Loops List
a = ['cat', 'window', 'defenestrate']
for x in a:
    print (x, len(x))

#知识点:

#    * 条件和循环语句
#    * 如何得到控制台输入
