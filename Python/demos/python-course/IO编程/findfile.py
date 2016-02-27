# -*- coding: utf-8 -*-

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os
import sys
from collections import deque

def find_file(path, name):
    for file_name in os.listdir(path):
        sub_path = os.path.join(path, file_name)
        if file_name.lower().find(name) != -1:
            print(sub_path)
        if os.path.isdir(sub_path):
            find_file(sub_path, name)

#非递归实现：list
def find_file_loop(path, name):
    paths = [ path ]
    while len(paths) > 0:
        top_path = paths.pop()
        for file_name in os.listdir(top_path):
            sub_path = os.path.join(top_path, file_name)
            if file_name.lower().find(name) != -1:
                print(sub_path)
            if os.path.isdir(sub_path):
                paths.append(sub_path)

#非递归实现：queue
def find_file_deque(path, name):
    paths = deque([path])
    while len(paths) > 0:
        top_path = paths.pop()
        for file_name in os.listdir(top_path):
            sub_path = os.path.join(top_path, file_name)
            if file_name.lower().find(name) != -1:
                print(sub_path)
            if os.path.isdir(sub_path):
                paths.append(sub_path)

def main():
    path = ''
    name = ''
    args = sys.argv
    if len(args) == 2:
        name = args[1]
        path = os.getcwd()
    elif len(args) == 3:
        name = args[1]
        path = args[2]
    else:
        print('wrong arguments')
        exit(-1)
    find_file(path, name)

if __name__ == '__main__':
    main()
