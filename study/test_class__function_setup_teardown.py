#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:29
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_class__function_setup_function_teardown_function.py
import pytest

'''从运行结果看出，setup_module/teardown_module的优先级是最大的，
然后函数里面用到的setup_function/teardown_function与
类里面的setup_class/teardown_class互不干涉'''
def setup_module():
    print("setup_module：整个.py模块只执行一次11")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次11")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行22")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行22")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = 3
    assert (x, 3)

class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前33")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前33")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = 3
        assert (x, 3)

if __name__ == "__main__":
    pytest.main(["-s", "test_class__function_setup_teardown"])