# -*- coding: utf-8 -*-

#利用os模块编写一个能实现ls -l输出的程序。
# total 4
# drwxrwxrwx   221   Bauer   Administrator      772393  2016-01-07 23:31:58  demos
# drwxrwxrwx     6   Bauer   Administrator     7382673  2016-01-17 21:01:05  doc
# -rw-rw-rw-     1   Bauer   Administrator        2210  2016-01-17 22:14:08  ls.py
# drwxrwxrwx     2   Bauer   Administrator     1430505  2016-01-03 01:11:30  thirdparty

import os
import stat
import sys
from datetime import datetime

_file_ower_table_ = {
    0 : 'Bauer',
}

_file_group_table_ = {
    0 : 'Administrator'
}

def get_file_number(path):
    """求一个路径包含的文件和文件夹数量"""
    number = 1
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            number += get_file_number(os.path.join(path, sub_path))
    return number

def get_file_mode(path):
    return stat.filemode(os.stat(path).st_mode)

def get_file_ower(path):
    uid = os.stat(path).st_uid
    return _file_ower_table_.get(uid, 'None')

def get_file_group(path):
    gid = os.stat(path).st_gid
    return _file_group_table_.get(gid, 'None')

def get_file_size(path):
    if os.path.isdir(path):
        total_size = 0
        for subPath in os.listdir(path):
            total_size += get_file_size(os.path.join(path, subPath))
        return total_size
    else:
        return os.stat(path).st_size

def get_file_mtime(path):
    timestamp = os.stat(path).st_mtime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_file_name(path):
    return os.path.basename(path)

def ls(path):
    print('{}{:>6}  {:>6}  {:>14}{:>12}  {}  {}'.format(
        get_file_mode(path),
        get_file_number(path),
        get_file_ower(path),
        get_file_group(path),
        get_file_size(path),
        get_file_mtime(path),
        get_file_name(path)
    ))

def main():
    path = ''
    args = sys.argv
    if len(args) == 1:
        path = os.getcwd()
    elif len(args) == 2:
        if os.path.isabs(path):
            path = args[1]
        else:
            path = os.path.join(os.getcwd(), args[1])
    else:
        print('wrong arguments')
        exit(-1)
    print('total {}'.format(get_file_number(path)))
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            ls(os.path.join(path, sub_path))
    else:
        ls(path)

if __name__ == '__main__':
    main()

