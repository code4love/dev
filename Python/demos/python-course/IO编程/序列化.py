# -*- coding: utf-8 -*-

import pickle
#dump返回的是bytes,必须已'b'的方式打开才能直接写入
with open('dump.txt', 'wb') as f:
    d = dict(name='Bob', age=20, score=88)
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

#pickle如何序列化自定义类???


#Json格式的序列化和反序列化
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
#Out: '{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str)
print(s)
#Out: {'age': 20, 'score': 88, 'name': 'Bob'}

#JSON进阶:格式化自定义类
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'name:{}, age:{}, score:{}'.format(self.name, self.age, self.score)

#定义将Student对象转化为dict的函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str, object_hook=dict2student)
print(s)

#Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。