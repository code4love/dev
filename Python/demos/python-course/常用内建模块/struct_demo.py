# -*- coding: utf-8 -*-

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

# struct的pack函数把任意数据类型变成bytes：
import struct
print(struct.pack('>I', 10240099))
#Out: b'\x00\x9c@c'
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

#unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#Out: (4042322160, 32896)
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。


# 实例:
# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
# 首先找一个bmp文件，没有的话用“画图”画一个。
# 读入前30个字节来分析：

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
#
# 所以，组合起来用unpack读取：

print(struct.unpack('<ccIIIIIIHH', s))
# Out: (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
# 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。