#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 19:45
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_mixt.py
import pytest

'''1.firture相对于setup和teardown来说应该有以下几点优势
命名方式灵活，不局限于setup和teardown这几个命名
conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
scope="module" 可以实现多个.py跨文件共享前置
scope="session" 以实现多个.py跨文件使用一个session来完成多个用例'''


'''用例1需要先登录，用例2不需要登录，用例3需要先登录'''
# 不带参数时默认scope="function"

@pytest.fixture()#如果@pytest.fixture()里面没有参数，那么默认scope="function"，也就是此时的级别的function，针对函数有效
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_mixt.py"])