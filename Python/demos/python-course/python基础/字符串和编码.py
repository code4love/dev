# -*- coding: utf-8 -*-

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
#Out: 65
print(ord('中'))
#Out: 20013
print(chr(66))
#Out: 'B'
print(chr(25991))
#Out: '文'

#由于Python的字符串在内存中以Unicode表示，一个字符对应若干个字节。
#unicode是一种字符的内存存储方式，并不是编码方式。常见编码方式:ascii,utf-8,gbk,gb2312
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)
#注意区分'ABC'和b'ABC'，前者6个字节，后者3个

#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))
#Out: b'ABC'
print('中文'.encode('utf-8'))
#Out: b'\xe4\xb8\xad\xe6\x96\x87'
#print('中文'.encode('ascii'))
#Out: UnicodeEncodeError
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围

#要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
#Out: 3
print(len('中文'))
#Out: 2
#len()函数针对str计算字符数，针对bytes计算字节数：
print(len('中文'.encode('utf-8')))
#Out:6

#把bytes变为str，用decode()方法
print(b'ABC'.decode('ascii'))
#Out: 'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#Out: '中文'

#字符串中出现'\u'表示后面为unicode编码
print('\u4e2d\u6587')
#Out: '中文'