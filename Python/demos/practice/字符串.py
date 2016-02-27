#比起C/C++,Python处理字符串的方式实在太让人感动了.
# 字符串操作类似列表操作,但字符串是只读的
#! /usr/bin/python

word="abcdefg"
a=word[2]
print ("a is: "+a)
b=word[1:3]
print ("b is: "+b) # index 1 and 2 elements of word.
c=word[:2]
print ("c is: "+c) # index 0 and 1 elements of word.
d=word[0:]
print ("d is: "+d) # All elements of word.
e=word[:2]+word[2:]
print ("e is: "+e) # All elements of word.
f=word[-1]
print ("f is: "+f) # The last elements of word.
g=word[-4:-2]
print ("g is: "+g) # index 3 and 4 elements of word.
h=word[-2:]
print ("h is: "+h) # The last two elements.
i=word[:-2]
print ("i is: "+i) # Everything except the last two characters
l=len(word)
print ("Length of word is: "+ str(l))

#中文和英文的字符串长度是否一样?
#! /usr/bin/python
# -*- coding: utf8 -*-
print ("len of 中国:", len("中国"))

"""
知识点:
•	类似Java,在python3里所有字符串都是unicode,所以长度一致.
"""

#string 常用函数举例
s = "hello world"
print("capitalize:", s.capitalize())
print("center:", s.center(21, "-"))
print("encode ascii", s.encode("ascii"))
print("ends with world:", s.endswith("world"))
print("start with Hello:", s.startswith("Hello"))
#expandtabs Return a copy of the string
#where all tab characters are replaced by one or more spaces
print("expandtabs", s.expandtabs())
print("find find:", s.find("llo")) #return -1 if not found
print("llo index:", s.find("llo")) #Raise ValueError if not found
print("formated:", "{0} + {1} = {2}".format(1, 2, 3))
print("isalnum():", s.isalnum())
print("isdigit():", s.isdigit())
print("isdecimal():", s.isdecimal())
print("isalpha():", s.isalpha())
print("isnumeric():", s.isnumeric())
print("isspace():", s.isspace())
print("istitle():", s.istitle())
print("isupper():", s.isupper())
print("islower():", s.islower())
print("join():", s.join(" hello earth"))  #what does join do???

s = s.upper()
print("upper:", s)
s = s.ljust(20, "-")
print("ljust:", s)
s = s.rstrip("-")
print("rtrip:", s)

s = s.replace("WORLD", "world")
print("replace:", s)
print("rfind:", s.rfind("world"))

print("split", s.split())
