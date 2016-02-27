# -*- coding: utf-8 -*-


#---return---
#函数体内部可以用return随时返回函数结果
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。


#---参数检查---
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
#但是如果参数类型不对，Python解释器就无法帮我们检查
#可以在函数定义时手动检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#my_abs("abc") raise TypeError('bad operand type')


#---返回多个值---
#函数可以返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)
#Out:(151.96152422706632, 70.0)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号
#而多个变量可以同时接收一个tuple，按位置赋给对应的值
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


#exercise
#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解
#该不该在函数内部捕获异常？？？
import math
def quadratic(a, b, c):
    #先检查参数类型
    for i in a, b, c:
        if not isinstance(i, (int, float)):
            raise ValueError('param must be a valid number')
    if a == 0:
        try:
            x = -c/b
            return -c/b,-c/b
        except ZeroDivisionError as err:
            print(err)
            return
    else:
        try:
            sqrt = math.sqrt(b*b - 4*a*c)
        except ValueError as err:
            print(err)
            return  #same to return None
        x1 = (-b + sqrt) / (2*a)
        x2 = (-b - sqrt) / (2*a)
        return x1, x2

print(quadratic(0, 0, 3))
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(3, 5, 11))
