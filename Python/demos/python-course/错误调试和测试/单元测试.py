# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    #每一个测试方法前都会调用
    def setUp(self):
        print('setUp...')

    #每一个测试方法后都会调用
    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    #此方法不会调用,因为只会运行已'test'开始的方法名
    def mytestfunc(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 2)

#编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
#对每一类测试都需要编写一个test_xxx()方法

#------------------运行单元测试------------------
#最简单的运行方式是在测试模块的最后加上两行代码：
# if __name__ == '__main__':
#     unittest.main()

#另一种方法是在命令行通过参数-m unittest直接运行单元测试：
#这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。