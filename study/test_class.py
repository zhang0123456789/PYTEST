#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 18:05
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_class.py


'''pytest用例规则
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用assert
所有的包pakege必须要有__init__.py文件'''

import pytest
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

'''cmd执行pytest用例有三种方法,以下三种方法都可以，一般推荐第一个
1、pytest
2、py.test
3、python -m pytest如果不带参数，在某个文件夹下执行时，它会查找该文件夹下所有的符合条件的用例（查看用例设计原则）'''