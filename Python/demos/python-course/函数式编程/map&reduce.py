# -*- coding: utf-8 -*-

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

#把这个list所有数字转为字符串：
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
#Out: 25

#map配合reduce将字符串转换为整数:
from functools import reduce
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('13579'))
#Out: 13579


#---------练习1---------
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
print(list(map(str.capitalize, ['adam', 'LISA', 'barT'])))

#---------练习2---------
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l):
    def multipe(x, y):
        return x * y
    return reduce(multipe, l)
print(prod([2, 3, 5, 8]))

#---------练习3---------
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    point = 0
    def to_float(x, y):
        #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        #不加nonlocal这里会有语法错误
        nonlocal point
        if y==-1:
            point = 1
            return x
        if point==0:
            return x*10 + y
        else:
            point = point*10
            return x + y/point
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':-1}[s]
    return reduce(to_float, map(char2num, s), 0.0)

print(str2float('123.456'))