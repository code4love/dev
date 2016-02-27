# -*- coding: utf-8 -*-

#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student(object):
    pass

#尝试给实例绑定一个属性：
s = Student()
s.name = "Jack Chen"
print(s.name)

#还可以尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
#s2.set_age(24)  AttributeError

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, Student)
s.set_score(90)
s2.set_score(100)
print(s.score)
print(s2.score)
#输出结果都为100可以看出绑定的是静态方法
#如何动态增加类方法？？？

#----------使用__slots__-----------
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Person(object):
    __slots__ = ('__name', '__age')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "name:{},age:{}".format(self.__name, self.__age)

s = Person("Mary", 20)
print(s)
#s.address = "NY"   语法错误,__slots__限制了Person的属性只有__name和__age

#注意:__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

