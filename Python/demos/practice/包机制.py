#每一个.py文件称为一个module,module之间可以互相导入.请参看以下例子:
# a.py
#def add_func(a,b):
#    return a+b

# b.py
from a import add_func # Also can be : import a

print ("Import add_func from module a")
print ("Result of 1 plus 2 is: ")
print (add_func(1,2))    # If using "import a" , then here should be "a.add_func"


#module可以定义在包里面.Python定义包的方式稍微有点古怪,假设我们有一个parent文件夹,
#该文件夹有一个child子文件夹.child中有一个module a.py .
#如何让Python知道这个文件层次结构?很简单,每个目录都放一个名为_init_.py 的文件.
#该文件内容可以为空.这个层次结构如下所示:
#parent
#  --__init_.py
#  --child
#    -- __init_.py
#    --a.py

#b.py

#那么Python如何找到我们定义的module?在标准包sys中,path属性记录了Python的包路径.你可以将之打印出来:

import sys

print(sys.path)

#通常我们可以将module的包路径放到环境变量PYTHONPATH中,该环境变量会自动添加到sys.path属性.
# 另一种方便的方法是编程中直接指定我们的module路径到sys.path 中:
import sys
import os
sys.path.append(os.getcwd()+'\\parent\\child')

print(sys.path)

from a import add_func


print (sys.path)

print ("Import add_func from module a")
print ("Result of 1 plus 2 is: ")
print (add_func(1,2))

"""
知识点:
•	如何定义模块和包
•	如何将模块路径添加到系统路径,以便python找到它们
•	如何得到当前路径
"""
