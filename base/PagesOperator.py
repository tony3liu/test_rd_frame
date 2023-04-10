# coding: utf-8
# 页面属性封装(url, 浏览器实例, 元素, 操作)
# 页面调用(页面继承，页面实例化)
# 基于页面调用实现的两种方式
# import selenium.webdriver
import time
# import pytest
from base import browsers
from setting import *


class Page:
    url = None  # 页面地址的初始化
    driver = None  # 浏览器驱动的初始化实例

    def element(self, location_ele: tuple):
        """

        :param location_ele: 单个定位元素
        :return:
        """
        return self.driver.find_element(*location_ele)

    def elements(self, location_eles: tuple):
        """

        :param location_eles: 定位的元素组
        :return:
        """
        return self.driver.find_elements(*location_eles)


class CommonLoginPage(Page):
    url = PROJECT_ZENTAO_URL
    driver = browsers.CHROME().browsers  # 直接使用封装好的浏览器对象
    username = ('id', 'account')
    password = ('name', 'password')
    submit_button = ('id', 'submit')

    def get(self):
        """
        打开url地址
        :return:
        """
        self.driver.get(self.url)
        time.sleep(10)

    def login(self, username='liutao', password='smAI2021'):
        self.get()
        self.element(self.username).send_keys(username)
        self.element(self.password).send_keys(password)
        self.element(self.submit_button).click()
        time.sleep(10)


class PagesOperator(CommonLoginPage):
    test_app_menu = ('xpath', '//*[@id="menuMainNav"]/li[5]/a/span')
    assert_ele = ('xpath', "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")

    # 下面是具体页面的业务操作方法
    def po_going_qa_app(self):
        self.login()
        self.element(self.test_app_menu).click()
        time.sleep(5)
        self.driver.quit()


# # 下面是测试用例
# class TestCase(PagesOperator):
#
#     def test_going_test_app(self):
#         self.po_going_qa_app()
#         assert self.element(self.assert_ele).text == '测试统计'
#
#
# # debug
# if __name__ == "__main__":
#     pytest.main('./PagesOperator.py')
