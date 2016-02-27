# -*- coding: utf-8 -*-

#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
#可用collections模块的Iterable类型判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
#out:True
print(isinstance([1,2,3], Iterable)) # list是否可迭代
#out:True
print(isinstance(123, Iterable)) # 整数是否可迭代
#out:False

#迭代字符串
for ch in 'ABC':
    print(ch, end=" ")
print()

#迭代元组
for n in (1, 2, 3):
    print(n, end=" ")
print()

#迭代dict
dict = {'Jack' : 30, 'Jason' : 28, 'Mary' : 22}
for key in dict:
    print(key, end=" ")
print()

for value in dict.values():
    print(value, end=" ")
print()

for key, value in dict.items():
    print(key, value, end=" ")
print()


#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value, end=" ")
print()

#for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y, z in [(1, 1, 2), (2, 4, 6), (3, 9, 12)]:
    print(x, y, z, end="\t")