# -*- coding: utf-8 -*-

#StringIO是在内存中读写str
#BytesIO是在内存中读写bytes

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
#Out: hello world!

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


#写BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#Out: b'\xe4\xb8\xad\xe6\x96\x87'


#读BytesIO
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
#Out: b'\xe4\xb8\xad\xe6\x96\x87'
