#! /usr/bin/python
# -*- coding: utf8 -*-
#列表类似Javascript的数组,方便易用

numbers = [0, 1, 2, 3, 4, 5, 6]
print("numbers[1:4]:", numbers[1:4])
print("numbers[1:]:", numbers[1:])
print("numbers[1:1]:", numbers[1:1])
print("numbers[1:2]:", numbers[1:2])
print("numbers[-1]:", numbers[-1])
print("numbers[-1: -3]:", numbers[-1: -3])
#为什么-1:1是空的，1:-1却有元素？？？
print("numbers[-1: 1]:", numbers[-1: 1])
print("numbers[1: -1]:", numbers[1: -1])
numbers.insert(1, 10)
print("numbers after inserted:", numbers)
numbers.pop(1) #equals del numbers[1]
print("numbers after pop:", numbers)

print("index of 5 is", numbers.index(5))

numbers.remove(5)
print("numbers after remove 5", numbers)

numbers.insert(5, 5)
print("numbers after insert 5", numbers)

numbers.append(7)
print("numbers after after append", numbers)

numbers.extend([8, 9, 10])
print("numbers after after extend", numbers)

numbers.reverse()
print("numbers after after reverse", numbers)

numbers.sort()
print("numbers after after sort", numbers)

'''
知识点:

    * 列表长度是动态的,可任意添加删除元素.
    * 用索引可以很方便访问元素,甚至返回一个子列表
    * 更多方法请参考Python的文档
'''
