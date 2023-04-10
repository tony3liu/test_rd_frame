# 本模块为固定写法，需要熟练
import unittest
import os
# from unittest_case import tests
from setting import *
import HtmlTestRunner

# path
CASE_PATH = os.path.join(os.getcwd(), './unittest_case')
# 初始化组件
suit = unittest.TestSuite()
loader = unittest.TestLoader()

# operate
for t in SUIT_PROJECT_2:
    suit_content_load = loader.discover(CASE_PATH, pattern=t)
    suit.addTest(suit_content_load)

# with open("./report.txt", "w") as fp:
#     runner = unittest.TextTestRunner(fp, verbosity=2)  # 初始化测试报告，并将测试结果以数据流的形式写进测试报告
#     runner.run(suit)

runner = HtmlTestRunner.HTMLTestRunner(verbosity=2)
runner.run(suit)
