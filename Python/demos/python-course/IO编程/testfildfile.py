# -*- coding: utf-8 -*-

import unittest
import findfile

class TestFindFile(unittest.TestCase):

    def setUp(self):
        self.dir_path = r"D:\taocode\trunk"
        self.find_name = 'python'

    def test_find_file(self):
        findfile.find_file(self.dir_path, self.find_name)

    def test_find_file_loop(self):
        findfile.find_file_loop(self.dir_path, self.find_name)

    def test_find_file_deque(self):
        findfile.find_file_deque(self.dir_path, self.find_name)

# if __name__ == '__main__':
#     unittest.main()

