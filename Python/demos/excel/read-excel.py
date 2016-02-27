# -*- coding: utf-8 -*-

# 安装
#   pip install xlrd

# 二、使用介绍
#   1、导入模块
#       import xlrd
#    2、打开Excel文件读取数据
#        data = xlrd.open_workbook('excelFile.xls')
#    3、使用技巧
#         获取一个工作表
#         table = data.sheets()[0]          #通过索引顺序获取
#         table = data.sheet_by_index(0) #通过索引顺序获取
#         table = data.sheet_by_name(u'Sheet1')#通过名称获取
#         获取整行和整列的值（数组）
#          table.row_values(i)
#          table.col_values(i)
#         获取行数和列数
#         nrows = table.nrows
#         ncols = table.ncols
#         循环行列表数据
#         for i in range(nrows ):
#       print table.row_values(i)
# 单元格
# cell_A1 = table.cell(0,0).value
# cell_C4 = table.cell(2,3).value
# 使用行列索引
# cell_A1 = table.row(0)[0].value
# cell_A2 = table.col(1)[0].value

# 更过实例查看安装目录下的example

import xlrd

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def main():
    excel = open_excel('test.xlsx')
    table = excel.sheets()[0]
    for i in range(table.nrows):
        print(table.row_values(i))

if __name__=='__main__':
    main()