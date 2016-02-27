# -*- coding: utf-8 -*-


#----------__len__()----------
class Foo(object):
    def __init__(self, len):
        self.len = len
    def __len__(self):
        return self.len
print(len(Foo(3)))


#----------__str__()----------
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
s = Student("Jack Chen")
#>>>s       #call __repr__
print(s)    #call __str__


#----------__iter__()----------
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n, end=" ")
print()


#----------__getitem__()----------
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[5])
#out: 5
print(f[2:5])
#out: [2, 3, 5]


#----------__getattr__()----------
#python中调用一个不存在的属性时会抛出AttributeError，例如
class Person(object):
    def __init__(self):
        self.name = 'Michael'
p = Person()
#print(p.score) AttributeError
class Person(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
p = Person()
print(p.score)  #99

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
#Out: '/status/user/timeline/list'


#----------__call__()----------
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

    #__call__还可以加参数
    #def __call__(self, age):
    #    print('My name is {}, age is {}'.format(self.name, age))

s = Student("Jason Bourne")
s()  #call s.__call__

#使用callable判断一个对象是否能被调用
print(callable(s))          #True
print(callable(max))        #True
print(callable([1, 2, 3]))  #False