#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:06
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_fixt.py

import pytest
def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束后都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

if __name__ == "__main__":
    pytest.main(["-s", "test_fixt.py"])#-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
