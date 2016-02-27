# -*- coding: utf-8 -*-

import itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

# 首先，我们看看itertools提供的几个“无限”迭代器：
if False:
    natuals = itertools.count(1)
    for n in natuals:
        print(n, end=' ')
#Out:1 2 3 4....  #停不下来

#cycle()会把传入的一个序列无限重复下去：
if False:
    cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    for c in cs:
        print(c, end=' ')
#Out: A B C A B C...


#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
if False:
    ns = itertools.repeat('A', 3)
    for n in ns:
        print(n, end=' ')
#Out: A A A

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
#Out: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c, end=' ')
print()
#Out: A B C X Y Z

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print('{}:{}'.format(key, list(group)))
# Out:
# A:['A', 'A', 'A']
# B:['B', 'B', 'B']
# C:['C', 'C']
# A:['A', 'A', 'A']

# 指定判断key是否相同的函数
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
# Out:
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']

#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。