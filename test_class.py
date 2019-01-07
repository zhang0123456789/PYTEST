#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 18:05
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_class.py


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')