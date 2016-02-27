#! /usr/bin/python

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
flag = a == b == c == d == e
print(flag)

print("len of a is:", len(a))
flag = "four" in a
print(flag)

a["four"] = 4
print("dict after add four", a)

a.pop("four") #del a["four"]
print("dict atter remove four", a)

e = a.copy()
print("e:", e)
e.clear()
print("e after clear:", e)

print("items:", a.items())
print("keys:", a.keys())
print("values:", a.values())

