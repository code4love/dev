# -*- coding: utf-8 -*-

class Student:
    teacher = "Jack Chen"
    #类方法必然以self作为第一个参数
    @classmethod
    def student(self):
        print("student")

    #静态方法没有self参数
    #添加staticmethod tag才会没有警告
    @staticmethod
    def func():
        print("Student:func")

#静态方法可以通过类名直接调用，也可以通过对象调用
Student.func()
Student().func()

s = Student()
print(s.teacher)

#这样赋值之后实际上是给s增加了一个成员变量,而Student的静态变量teach并没有改变
s.teacher = "Jason bauer"
print(s.teacher)
#Out: Jason Bourne
print(Student.teacher)
#OUt: Jack Chen

Student.teacher = "Jack Bauer"
print(Student.teacher)
#OUt: Jack Bauer

#所以静态变量不能和成员变量同名！！！