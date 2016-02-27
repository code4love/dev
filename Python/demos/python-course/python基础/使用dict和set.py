# -*- coding: utf-8 -*-

#dict内部存放的顺序和key放入的顺序没有关系

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#dict 的key和value都可以是不同类型
d[3] = 'Jason'
print(d)

#print(d['Thomas']) key不存在时报错

#检查key是否存在
print('Thomas' in d)
#Out: False

#使用get()
d.get('Thomas')         #return null
d.get('Thomas', -1)     #return -1

#使用pop
value = d.pop('Bob')
print(value)

#dict的key必须是不可变对象

#list是可变的,不可作为key
list = [1, 2, 3]
#d[l] = 'Mary' raise TypeError

#tuple是不可变的,可以作为key
tuple = (1, 2, 3)
d[tuple] = 'Mary'
print(d)

#----------------------set----------------------
#set元素是无序的,可以是不同类型,重复的元素会自动去重
set = {'abc', 2, 3, 3, 1}
print(set)
#Out: {1, 2, 3}

#set不能直接赋值
#set[2] = 5 TypeError: 'set' object does not support item assignment

set.add(4)      #添加元素4
set.remove(4)   #删除元素4

set.pop() #删除第一个元素,pop不可带参数

#set的原理和dict一样，所以，同样不可以放入可变对象
#set.add([1, 2, 3]) #list可变,TypeError
set.add((1, 2, 3))  #tuple不可变,ok
print(set)
