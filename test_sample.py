#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/7 0007 下午 17:56
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : test_sample.py


'''非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
能够支持简单的单元测试和复杂的功能测试
支持参数化
执行测试过程中可以将某些测试跳过（skip），或者对某些预期失败的case标记成失败
支持重复执行(rerun)失败的case
支持运行由nose, unittest编写的测试case
可生成html报告
方便的和持续集成工具jenkins集成
可支持执行部分用例
具有很多第三方插件，并且可以自定义扩展'''


'''打开test_sample.py所在的文件夹，cmd窗口输入：pytest（或者输入py.test也可以）
pytest运行规则：**查找当前目录及其子目录下以test_*.py或*_test.py文件，找到文件后，
在文件中找到以test开头函数并执行。**'''
def func(x):
    return  x+1

def test_answer():
    assert  func(3)==5