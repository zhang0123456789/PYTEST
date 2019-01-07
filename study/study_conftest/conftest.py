#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:53
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : conftest.py

import pytest


@pytest.fixture()
def login():
    print("输入账号，密码先登录")
