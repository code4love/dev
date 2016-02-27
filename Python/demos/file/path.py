import os
a, b = os.path.split( r"c:\123\456\test.txt" )
print(a)
print(b)

a, b = os.path.splitext( r"test.txt" )
print(a)
print(b)

b = os.path.exists( r"C:\test")
print(b)

b = os.path.isfile(r"C:\Windows\system.ini")
print(b)

b = os.path.isdir(r"C:\Windows\system.ini")
print(b)

l = os.listdir(r"C:\Windows")
print(l)