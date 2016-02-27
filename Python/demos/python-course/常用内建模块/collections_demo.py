# -*- coding: utf-8 -*-


# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# ---------------namedtuple---------------
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('({}, {})'.format(p.x, p.y))


# ---------------deque---------------
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储
# 数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.pop()
q.popleft()
q.append('x')
q.appendleft('y')
print(q)


# ---------------defaultdict---------------
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
#Out: 'abc'
print(dd['key2'])    # key2不存在，返回默认值
#Out: 'N/A'


# ---------------OrderedDict---------------
# dict是无序的.如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = {1 : 'a', 3 : 'c', 2 : 'b'}
print(d)
#Out: {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([(1, 'a'), (3, 'c'), (2, 'b')])
print(od) # OrderedDict的Key是有序的
#Out: OrderedDict([(1, 'a'), (3, 'c'), (2, 'b')])


# ---------------Counter---------------
# Counter是一个简单的计数器，实际上也是dict的一个子类
# 统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
#Out: Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})