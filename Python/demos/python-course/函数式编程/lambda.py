# -*- coding: utf-8 -*-

#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
f = lambda x:x*x
#相当于
def f(x):
    return x*x

f = lambda x, y:x+y
#相当于
def f(x,y):
    return x+y

#实例1,使用reduce求和
from functools import reduce
print(reduce(lambda x,y:x+y, [1, 3, 5, 6, 9]))

#实例2,用sorted()对下述列表按分数有高到低排序：
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(l, key = lambda t: t[1], reverse=True))