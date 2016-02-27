import  shutil
import  os
import  os.path

src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "dst.txt")
dst2 = os.path.join(os.getcwd(), "dst2.txt")

dir1 = os.path.dirname(src)

print ( " dir1 %s " % dir1)

if not os.path.exists(src):
    os.makedirs(dir1)

f1 = open(src, "w" )
f1.write( " line a\n " )
f1.write( " line b\n " )
f1.close()

shutil.copyfile(src, dst)
shutil.copyfile(src, dst2)
f2 = open(dst, "r" )
for  line  in  f2:
     print (line)

f2.close()

# 测试复制文件夹树
try :
    srcDir = os.path.join(os.getcwd(), "scrDir")
    dstDir = os.path.join(os.getcwd(), "dstDir")
    if not os.path.exists(srcDir):
        os.makedirs(srcDir)
     # 如果dstDir已经存在,那么shutil.copytree方法会报错!
     # 这也意味着你不能直接用d:作为目标路径.
    shutil.copytree(srcDir, dstDir)
except  Exception as err:
     print  (err)

'''
    知识点:
    * shutil.copyfile:如何复制文件
    * os.path.exists:如何判断文件夹是否存在
    * shutil.copytree:如何复制目录树
'''

"""
总结:4个函数
•	os.path.dirname(path)
•	os.path.exists(path)
•	shutil.copyfile(src, dst)
•	shutil.copytree(srcDir, dstDir)
 """
