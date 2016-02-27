import  os.path
# 常用函数有三种:分隔路径,找出文件名.找出盘符(windows系统),找出文件的扩展名.
# 根据你机器的实际情况修改下面参数.
spath = " D:/download/repository.7z "

#  case 1:
p,f = os.path.split(spath)
print ( " dir is: " + p)
print ( " file is: " + f)

#  case 2:
drv,left = os.path.splitdrive(spath)
print ( " driver is: " + drv)
print ( " left is: " + left)
#  case 3:
f,ext = os.path.splitext(spath)
print ( " f is: " + f)
print ( " ext is: " + ext)
'''
    知识点:    这三个函数都返回二元组.
    * case1 分隔目录和文件名
    * case2 分隔盘符和文件名
    * case3 分隔文件和扩展名
'''

"""
总结:5个函数
•	os.walk(spath)
•	os.path.split(spath)
•	os.path.splitdrive(spath)
•	os.path.splitext(spath)
•	os.path.join(path1,path2)
 """
