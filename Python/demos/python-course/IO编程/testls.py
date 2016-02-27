# -*- coding: utf-8 -*-

import unittest
import ls
import datetime

class Testls(unittest.TestCase):

    def setUp(self):
        self.dir_path = r"D:\taocode\trunk\Python\doc"
        self.file_path = r"D:\taocode\trunk\Python\doc\python340.chm"

    def test_get_file_number(self):
        self.assertEqual(ls.get_file_number(self.dir_path), 6)
        self.assertEqual(ls.get_file_number(self.file_path), 1)

    def test_get_file_mode(self):
        self.assertEqual(ls.get_file_mode(self.dir_path), 'drwxrwxrwx')
        self.assertEqual(ls.get_file_mode(self.file_path), '-rw-rw-rw-')

    def test_get_file_ower(self):
        self.assertEqual(ls.get_file_ower(self.dir_path), 'Bauer')
        self.assertEqual(ls.get_file_ower(self.file_path), 'Bauer')

    def test_get_file_group(self):
        self.assertEqual(ls.get_file_group(self.dir_path), 'Administrator')
        self.assertEqual(ls.get_file_group(self.file_path), 'Administrator')

    def test_get_file_mtime(self):
        self.assertEqual(ls.get_file_mtime(self.dir_path), '2016-01-17 21:01:05')
        self.assertEqual(ls.get_file_mtime(self.file_path), '2014-03-22 09:40:26')

    def test_get_file_size(self):
        self.assertEqual(ls.get_file_size(self.dir_path), 7382673)
        self.assertEqual(ls.get_file_size(self.file_path), 7269706)

    def test_get_base_name(self):
        self.assertEqual(ls.get_file_name(self.dir_path), 'doc')
        self.assertEqual(ls.get_file_name(self.file_path), 'python340.chm')