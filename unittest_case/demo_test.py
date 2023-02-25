from time import sleep
import unittest_case
from base.PagesOperator2 import MainPage
import paramunittest


@paramunittest.parametrized(
    ('liutao', 'smAI2021', 'liutao'),
    ('zouxingli', 'zouzou', 'zouxingli')
)
class TestSearch(unittest_case.TestCase, MainPage):
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
        assert self.user_name.text == self.realname
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


if __name__ == '__main__':
    unittest_case.main()
