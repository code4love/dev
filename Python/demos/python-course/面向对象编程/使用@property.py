# -*- coding: utf-8 -*-

#Python内置的@property装饰器负责把一个方法变成属性调用
class Student(object):

    @property
    def score(self):
        print("call score getter")
        return self._score

    @score.setter
    def score(self, value):
        print("call score setter")
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score)

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

p = Person(20)
#p.age = 30  #错误，age是只读的
print(p.age)


#----------------练习----------------
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen:
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width*self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432