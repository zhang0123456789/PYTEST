#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 20:08
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_f3_teardown.py

import pytest


'''前面讲的是在用例前加前置条件，
相当于setup,既然有setup那就有teardown,fixture里面的
teardown用yield来唤醒teardown的执行'''


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

    yield
    print("执行teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f3_teardown.py"])