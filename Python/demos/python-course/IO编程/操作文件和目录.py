# -*- coding: utf-8 -*-

import os
print(os.name)      #操作系统类型
#os.name如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.environ)   #环境变量
print(os.environ.get('PATH'))

#列出所有的.py文件
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)