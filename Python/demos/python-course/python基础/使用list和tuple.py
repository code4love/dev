# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0])
#Out: 'Michael'
#print(classmates[3]) #raise IndexError

print(classmates[-1])
#Out: 'Tracy'
print(classmates[-len(classmates)])
#Out: 'Michael'
#print(classmates[-4]) #raise IndexError

classmates.append('Adam')
classmates.pop()
classmates.pop(1)
classmates.insert(1, 'Jason')

#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)

#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)

#tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
#其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)
#t[1] = 3 语法错误,元组元素不能更改
#定义空的元祖
t = ()
print(t)
#定义只有一个元素的元组
t = (1,)
print(t)

#一个元组可用这样赋值给多个元素
a, b, c = (1, 2, 3)
print(a, b, c, end=" ")

#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。