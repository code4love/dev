# -*- cording: utf-8 -*-

from collections import Iterable
from collections import Iterator
l = [1, 2, 3]
t = (1, 2, 3)
s = '123'
d = {'one' : 1, 'two' : 2, 'three':3}
set = {1, 2, 3}
g = (x for x in range(1, 3))
print(isinstance(l, Iterable))      #True
print(isinstance(t, Iterable))      #True
print(isinstance(s, Iterable))      #True
print(isinstance(d, Iterable))      #True
print(isinstance(set, Iterable))    #True
print(isinstance(g, Iterable))      #True

print(isinstance(l, Iterator))      #False
print(isinstance(t, Iterator))      #False
print(isinstance(s, Iterator))      #False
print(isinstance(d, Iterator))      #False
print(isinstance(set, Iterator))    #False
print(isinstance(g, Iterator))      #True

#能够使用for循环遍历的都是可迭代对象(Iterable)
#能够被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)
#生成器(generator)都是Iterator对象,但list,tuple,str,dict,set虽然是Iterable，却不是Iterator。

#可以使用iter()函数将list,tuple,str,dict,set变为Iterator
it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))


#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass

#实际上完全等价于：

#首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break