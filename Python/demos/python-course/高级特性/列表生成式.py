# -*- coding: utf-8 -*-

#生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))
#生成[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x*x for x in range(1, 11)])

#for循环后面还可以加上if判断
print([x*x for x in range(1, 11) if x%3==0])
#out: [9, 36, 81]

#还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])
#out: ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k, v in d.items()])
#out: ['y=B', 'x=A', 'z=C']

#把一个list中所有的字符串变成小写：
L = ['Hello', 2, 'World', 3, 'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s, str)])