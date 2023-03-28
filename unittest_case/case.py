# 下面有两个测试类，分别用了不同的参数化方法，
# 后期改造使用的时候，只能选择其中一种，另一种注释
# 下面的测试用例方法都是演示写法，不能直接执行，因为中间的业务逻辑关系没有理顺，比如前一条用例已经登出，后一条用例需要登录却没登录等等
# 所以在重新编排下面用例的时候，要遵循setupcls-->setup-->testcase_func-->teardown-->teardowncls的执行顺序

import unittest
from time import sleep
import paramunittest
import unittest_case
from base.PagesOperator2 import MainPage


@paramunittest.parametrized(
    ('liutao', 'smAI2021', 'liutao', 1350),
    ('zouxingli', 'zouzou', 'zouxingli', 1351)
)
class TestSearch(unittest.TestCase, MainPage):
    def setParameters(self, name, pwd, realname, bugid):
        """
        :param name:
        :param pwd:
        :param realname:
        :param bugid:
        :return:
        """
        self.name = name
        self.pwd = pwd
        self.realname = realname
        self.bugid = bugid

    @classmethod
    def setUpClass(cls) -> None:  # 测试类的前置方法，在整个测试类执行前被调用，类方法中只能调用类方法，所以里面要用到的方法都要再写一遍类方法
        cls.cls_get()
        cls.cls_login()

    def setUp(self) -> None:  # 测试用例的前置方法，在测试用例方法的执行前被调用
        self.get()
        self.login(username=self.name, password=self.pwd)

    @classmethod
    def tearDownClass(cls) -> None:  # 测试类的后置方法，在整个测试类执行后被调用，
        # 类方法中只能调用父类的类方法，所以里面要用到的方法都要再写一遍类方法、类属性、静态方法，不能使用实例方法
        cls.driver.quit()

    def tearDown(self) -> None:  # 测试用例的后置方法，在测试用例方法的执行后被调用
        self.login_out()
        self.driver.refresh()

    def test_search_bug(self):
        # 有了前置的登录操作，就不用再写登录了
        self.search_bug(self.bugid)
        assert self.bug_label.text == self.bugid,\
            self.driver.save_screenshot(f'./screenshot/{self.bugid}')

    def test_login(self):
        # 这是一个测试用例方法的编写例子，实际在有前置登录和后置退出的情况下，这条用例没有执行意义
        self.get()
        sleep(1)
        self.login(username=self.name, password=self.pwd)
        # 下面的断言随便写的例子，到时候自己去页面找正确的元素断言
        assert self.user_name.text == self.realname, \
            self.driver.save_screenshot(f'./screenshot/{self.realname}')
        self.login_out()
        sleep(1)


"""==========================================================================="""
# 用subTest进行参数化，要在测试用例中循环测试数据
# 测试用例在subTest()方法内执行。很粗暴的用法，每个用例都要写for循环+subTest();
# 好处是不用额外写固定的parametrized()方法,且由于用例本身是调用数据for循环，所以前置只会在测试用例方法前执行一遍
data = (
    {'name': 'liutao', 'pwd': 'smAI2021', 'realname': 'liutao', 'bugid': '1300'},
    {'name': 'zouxingli', 'pwd': 'zouzou', 'realname': 'zouxingli', 'bugid': '1301'}
)


class TestSearchSubTest(unittest.TestCase, MainPage):
    @classmethod
    def setUpClass(cls) -> None:
        ...

    def setUp(self) -> None:
        self.get()
        self.login()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def tearDown(self) -> None:
        self.login_out()
        self.driver.quit()

    def test_search_bug_two(self):
        for d in data:
            with self.subTest(d):
                self.search_bug(d['bugid'])
                assert self.bug_label.text == d['bugid'], \
                    self.driver.save_screenshot('./screenshot/{}'.format(d['bugid']))

    def test_login(self):
        # 这是一个测试用例方法的编写例子，实际在有前置登录和后置退出的情况下，这条用例没有执行意义
        for d in data:
            # 下面必须使用subTest()方法
            with self.subTest(d):
                self.get()
                sleep(1)
                self.login(username=d['name'], password=d['pwd'])
                # 下面的断言随便写的例子，到时候自己去页面找正确的元素断言
                # 断言成功就OK，断言失败就截图
                assert self.user_name.text == d['realname'], \
                    self.driver.save_screenshot('./screenshot/{}'.format(d['realname']))
                self.login_out()
                sleep(1)
                self.driver.quit()


if __name__ == '__main__':
    unittest_case.main()
