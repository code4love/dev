# -*- coding: utf-8 -*-


#---默认参数---
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L
# 当你正常调用时，结果似乎不错：
print(add_end([1, 2, 3]))
#Out: [1, 2, 3, 'END']
#当你使用默认参数调用时，一开始结果也是对的：
print(add_end())
#Out: ['END']
#再次调用add_end()时，结果就不对了：
print(add_end())
#Out: ['END', 'END']

#原因：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
#则下次调用时默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
#Out: ['END']


#---可变参数---
#可变参数只需在参数名前加'*'号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum
#参数个数可为0
print(calc())
#Out: 0
print(calc(1, 2, 3))

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3, 4]
print(calc(*nums))


#---关键字参数---
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#可只传必选参数
person('Michael', 30)
#Out: name: Michael age: 30 other: {}
#也可以传入任意个数的关键字参数：
person('Adam', 45, gender='M', job='Engineer')
#Out:name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
#注意:kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#---命名关键字参数---
#如果要限制关键字参数的名字，就可以用命名关键字参数:
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#person('Jack', 24, 'Beijing', 'Engineer') raise TypeError

#命名关键字参数可以有缺省值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')

#使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数。

#---参数组合---
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#可变参数无法和命名关键字参数混合，除此之外都可以组合使用
#但参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

args = (1, 2, 3, 4, 5)
kw = {'d': 99, 'x': '#'}
f1(-1, -2, *args, **kw)
#Out:a = -1 b = -2 c = 1 args = (2, 3, 4, 5) kw = {'d': 99, 'x': '#'}

#tuple前三个元素可以自动匹配参数a,b,c
f1(*args, **kw)
#Out:a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
args = (1, 2, 3)
kw = {'x': '#', 'd': 88}
#kw中的'd'先和命名关键字参数匹配
f2(*args, **kw)
#Out: a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

#def f3(*argc, *, a=1, b=2): #syntax error.可变参数不能和命名关键字参数混合
