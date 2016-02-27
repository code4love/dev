# -*- coding: utf-8 -*-

#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return "name:{},age:{}".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

s = Student("wuqiang", 20)
#print(s.__name)  #语法错误__name是私有的
print(s.get_name())
print(s)
