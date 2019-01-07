#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 18:52
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : hello.py


'''以xx.py脚本方式直接执行，当写的代码里面没用到unittest和pytest框架时，
并且脚本名称不是以test_开头命名的，此时pycharm会以xx.py脚本方式运行'''
def hello():
    print("hellod,world!")

if __name__ == '__main__':
    hello()
