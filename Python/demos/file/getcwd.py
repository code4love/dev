#取得当前目录，并在该目录生成一个按当前时间命名的文件夹
import os
import time

curr_dir = os.getcwd()
print("current dir:", curr_dir)
folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
os.makedirs(r'%s/%s'%(os.getcwd(),folder))