import os

def listdir(path):
    l = os.listdir(path)
    dirs = []
    for name in l:
        abs_path = os.path.join(path, name)
        if(os.path.isdir(abs_path)):
            dirs.append(name)
    return dirs


def listfile(path):
    l = os.listdir(path)
    files = []
    for name in l:
        abs_path = os.path.join(path, name)
        if(os.path.isfile(abs_path)):
            files.append(name)
    return files

path = r"E:\downloads"
print("dirs:")
print(listdir(path))
print("files:")
print(listfile(path))


