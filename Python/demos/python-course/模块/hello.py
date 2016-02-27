# -*- coding: utf-8 -*-

' a test module '

__author__ = 'wuqiang'

import sys

def test():
    args = sys.argv
    print("args:", args)
    #args[0]为本脚本文件的全路径
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
#而如果在其他地方导入该hello模块时，if判断将失败
if __name__=='__main__':
    test()