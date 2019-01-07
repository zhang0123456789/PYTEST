#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 20:05
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_f2.py

'''module级别的fixture在当前.py模块里，只会在用例（test_s2）第一次调用前执行一次'''
'''在用例前加前置条件，相当于setup'''
import pytest
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

def test_s1():
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3():
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f2.py"])