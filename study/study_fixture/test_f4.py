#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 20:11
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_f4.py


import pytest
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError  # 模拟异常

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f4.py"])