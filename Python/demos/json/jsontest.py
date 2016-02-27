import json

#python object to json str
data1 = {'b':789,'c':456,'a':123}
data2 = ["jack", "wang", "li"]
d1 = json.dumps(data1,sort_keys=True,indent=4)
d2 = json.dumps(data2,indent=4)
print(d1)
print(d2)

#json str to python object
data = json.loads(d1)
print(data)

a = ["a", "b", "c"]
b = a
a[0] = "A"
print(a)
print(b)