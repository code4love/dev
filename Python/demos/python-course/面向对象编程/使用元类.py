# -*- coding: utf-8 -*-

#----------------------type()----------------------
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#比方说我们要定义一个Hello的class，就写一个hello.py模块：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

#我们可以通过type()函数创建出Person类，而无需通过class Person(object)...的定义：
def init(self, name):
    self.__name = name

def get_name_s(self):
    return self.__name

Person = type('Person', (object,), dict(__init__=init, get_name=get_name_s))
p = Person("Jack Chen")
print(p.get_name())

# 要创建一个class对象，type()函数依次传入3个参数：
# 1, class的名称；
# 2, 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3, class的方法名称与函数绑定


#----------------------metaclass----------------------
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
#定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了
# 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

#测试:
L = MyList([1, 2, 3])
L.add(4)
print(L)
#Out: [1, 2, 3, 4]

# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
# 正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”，即对象-关系映射，
# 就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。