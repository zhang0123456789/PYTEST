#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:53
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_mixt1.py


import pytest


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == "__main__":
    pytest.main(["-s", "test_mixt1.py"])