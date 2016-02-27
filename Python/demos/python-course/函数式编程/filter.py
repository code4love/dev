# -*- coding: utf-8 -*-


#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#在一个list中，删掉偶数，只保留奇数:

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#Out: [1, 5, 9, 15]

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#---------练习---------
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    s = str(n)
    for i in range((len(s)+1)//2):
        if s[i] != s[-1-i]:
            return False
    return True

l = list(filter(is_palindrome, range(1, 1000)))
for i, value in enumerate(l):
    print('{:<4}'.format(value), end=" ")
    if (i+1)%10==0:
        print()