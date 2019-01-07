#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:54
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_mixt2.py


import pytest


def test_s4(login):
    print("用例4：登录之后其它动作111")


def test_s5():  # 不传login
    print("用例5：不需要登录，操作222")


if __name__ == "__main__":
    pytest.main(["-s", "test_mixt2.py"])