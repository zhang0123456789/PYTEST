#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 18:54
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_hello_unitest.py

'''pytest是可以兼容unittest框架代码的'''
import unittest

class Test1(unittest.TestCase):

    def test_hello(self):
        print("hello world")

if __name__ == '__main__':
    unittest.main()

