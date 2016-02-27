# -*- cording: utf-8 -*-

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()：
g = (x * x for x in range(5))
print(g)

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print(next(g))
#out: 0
print(next(g))
#out: 1
print(next(g))
#out: 4
print(next(g))
#out: 9
print(next(g))
#out: 16

#再调用next将raise StopIteration异常
#print(next(g))


#遍历一个生成器时常用的办法是使用for循环,而且不用关心StopIteration异常
g = (x * x for x in range(5))
for x in g:
    print(x)


#------------使用yield定义生成器------------
#一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator
#看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）# 才开始执行。
#虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值
#下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
#每次中断都会通过 yield 返回当前的迭代值。
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #每次执行到这里时返回迭代值b,下一次执行时从下一行代码执行
        a, b = b, a + b
        n = n + 1

#yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
#Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，
#而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
#执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
#而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。

#执行流程
f = fab(5)
print(next(f))
#Out: 1
print(next(f))
#Out: 1
print(next(f))
#Out: 2
#....

#或使用循环遍历
for n in fab(5):
    print(n, end = " ")
print()

#另一个实例
def yieldTest():
    yield 1
    yield 2
    for n in range(3, 10, 2):
        yield n

for n in yieldTest():
    print(n, end=" ")
#out: 1 2 3 5 7 9