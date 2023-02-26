# 下面有两个测试类，分别用了不同的参数化方法，
# 后期改造使用的时候，只能选择其中一种，另一种注释
import unittest
from time import sleep

import paramunittest

import unittest_case
from base.PagesOperator2 import MainPage


@paramunittest.parametrized(
    ('liutao', 'smAI2021', 'liutao'),
    ('zouxingli', 'zouzou', 'zouxingli')
)
class TestSearch(unittest.TestCase, MainPage):
    def setParameters(self, name, pwd, realname):
        """
        :参数化 注意这里接受参数的时候，必须要定义setParameters这个方法，并且只能是这个名称
        :param name:
        :param pwd:
        :param realname:
        """
        self.name = name
        self.pwd = pwd
        self.realname = realname

    def test_login_liutao(self):
        self.get()
        sleep(1)
        self.login(username=self.name, password=self.pwd)
        # 下面的断言随便写的例子，到时候自己去页面找正确的元素断言
        assert self.user_name.text == self.realname, \
            self.driver.save_screenshot('./screenshot')
        self.login_out()
        sleep(1)
        self.driver.quit()

    # def test_login_zouzou(self):
    #     # self.get() 上个用例已经打开了首页，并且完成用例后退出到了首页，不用重复打开
    #     self.login(username='zouxingli', password='zouzou')
    #     # 下面的断言随便写的例子，到时候自己去页面找正确的元素断言
    #     assert self.user_name.text == 'zouxingli'
    #     self.login_out()
    #     sleep(1)
    #     self.driver.quit()

"""==========================================================================="""
# 用subTest进行参数化，比较不好用，要在测试用例中循环测试数据
# 测试用例在subTest()方法内执行。很初级的用法，好处是不用额外写固定的parametrized()方法
data = (
    {'name': 'liutao', 'pwd': 'smAI2021', 'realname': 'liutao'},
    {'name': 'zouxingli', 'pwd': 'zouzou', 'realname': 'zouxingli'}
)


class TestSearchSubTest(unittest.TestCase, MainPage):
    def test_login(self):
        for d in data:
            # 下面必须使用subTest()方法
            with self.subTest(d):
                self.get()
                sleep(1)
                self.login(username=d['name'], password=d['pwd'])
                # 下面的断言随便写的例子，到时候自己去页面找正确的元素断言
                # 断言成功就OK，断言失败就截图
                assert self.user_name.text == d['realname'], \
                    self.driver.save_screenshot('./screenshot')
                self.login_out()
                sleep(1)
                self.driver.quit()


if __name__ == '__main__':
    unittest_case.main()
