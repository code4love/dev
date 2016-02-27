# -*- coding: utf-8 -*-

# 安装
#   pip install xlrd

# 简单使用
# import xlwt
# file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
# table = file.add_sheet('sheet name')  # 新建一个sheet
#
# table.write(0,0,'test')               # 写入数据table.write(行,列,value)
#
# # 如果对一个单元格重复操作，会引发
# # returns error:
# # Exception: Attempt to overwrite cell:
# # sheetname=u'sheet 1' rowx=0 colx=0
# # 所以在打开时加cell_overwrite_ok=True解决
#
# table = file.add_sheet('sheet name',cell_overwrite_ok=True)
# file.save('demo.xls')     # 保存文件
#
# # 另外，使用style
# style = xlwt.XFStyle()    # 初始化样式
# font = xlwt.Font()        # 为样式创建字体
# font.name = 'Times New Roman'
# font.bold = True
# style.font = font         #为样式设置字体
# table.write(0, 0, 'some bold Times text', style) # 使用样式

# 更过实例查看安装目录下的example

import xlwt
import os

file = xlwt.Workbook()
table = file.add_sheet('person', cell_overwrite_ok=True)
data = (('姓名', '性别', '年龄'), ('张三', '男', 22.0), ('李四', '男', 28.0), ('刘梅', '女', 20.0))
for i, row in enumerate(data):
    for j, value in enumerate(row):
        table.write(i, j, value)
file.save('person.xls')
