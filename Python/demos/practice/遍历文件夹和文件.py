import  os
import  os.path
#  os,os.path里包含大多数文件访问的函数,所以要先引入它们.
#  请按照你的实际情况修改这个路径
#  另一个遍历文件夹的函数os.listdir
rootdir = "E:/downloads"
for parent, dirnames, filenames in os.walk(rootdir):
     # case 1:
     for  dirname  in  dirnames:
         print( "parent is:", parent)
         print( "dirname is:", dirname)
     # case 2
     for  filename  in  filenames:
         print( "parent is:", parent)
         print( "filename with full path:", os.path.join(parent, filename))

''' 知识点:
    * os.walk返回一个三元组.其中dirnames是所有文件夹名字(不包含路径),
    filenames是所有文件的名字(不包含路径).parent表示父目录.
    * case1 演示了如何遍历所有目录.
    * case2 演示了如何遍历所有文件.
    * os.path.join(dirname,filename) : 将形如"/a/b/c"和"d.java"变成/a/b/c/d.java".
'''
