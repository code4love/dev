# -*- coding: utf-8 -*-

#一次读取全部
with open('test.log', 'r') as f:
    print(f.read())

#读取十个字节
with open('test.log', 'r') as f:
    print(f.read(10))

#按行读取
with open('test.log', 'r') as f:
    for line in f.readlines():
        print(line, end=" ")

#按gbk编码读取
with open('test.log', 'r', encoding='gbk') as f:
    print(f.read())

#读取二进制
with open ('test.jpg', 'rb') as f:
    #读取的是bytes流
    print(f.read(10))
#Out: b'\xff\xd8\xff\xe0\x00\x10JFIF'

#写文件
with open('test.txt', 'w') as f:
    f.write('Hello, world!')