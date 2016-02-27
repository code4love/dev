# -*- coding: utf-8 -*-

#方式一:
a = 2
f = 3.14
print("a=%d, f=%.3f"%(a,f))
#只有一个参数可省略括号
print("a=%d"%a)


#方式二(新方式,推荐):
#语法
#它通过{}和:来代替%。

#1,通过位置：
print('{0},{1}'.format('kzc',18))
#output:'kzc,18'
print('{},{}'.format('kzc',18))
#Out: 'kzc,18'
print('{1},{0},{1}'.format('kzc',18))
#Out: '18,kzc,18'

#2,通过关键字参数
print('{name},{age}'.format(age=18,name='kzc'))
print('a={a},b={b}'.format(a=2, b=3.14))
#Out: 'kzc,18'

#3,通过对象属性
class Person:
    def __init__(self, name, age):
        self.name,self.age = name,age
    def __str__(self):
        return 'This guy is {person.name},is {person.age} old'.format(person=self)
print(str(Person('kzc',18)))
#Out: 'This guy is kzc,is 18 old'

#4,通过下标
p=['kzc',18]
print('{0[0]},{0[1]}'.format(p))
#is same to:
print('{},{}'.format(p[0], p[1]))
#Out: 'kzc,18'

#5,填充与对齐
# 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
# 比如
print('{:>8}'.format('189'))
#Out: '   189'
print('{:0>8}'.format('189'))
#Out: '00000189'
print('{:#<8}'.format(189))
#Out: '189#####'
print('{:0>8}:{:0<8}'.format(101, 101))
#Out: '00000101:10100000'
#总结:'<'和'>'方向朝哪边字符串就往哪边靠

#6,精度与类型f
#精度常跟类型f一起使用
print('{:.2f}'.format(321.33345))
#Out: '321.33'

#7,其他类型
#主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。
print('{:b}'.format(17))
#Out: '10001'
print('{:d}'.format(17))
#Out: '17'
print(r'0{:o}'.format(17))
#Out: '21'
print('0x{:x}'.format(17))
#Out: '11'

#8,用','号做千位分隔符。
print('{:,}'.format(1234567890))
#Out[47]: '1,234,567,890'

#9,格式化类类型
list = [1, 2, 3]    #list use []
set = {1, 2, 3}     #set use {}
tuple = (1, 2, 3)   #tuple use()
dict = {'one':1, 'two':2, 'three':3} #dict use {}
print('list:{}\r\nset:{}\r\ntuple:{}\r\ndict:{}'.format(list, set, tuple, dict))
print('person:{}'.format(Person('jack', 30)))

