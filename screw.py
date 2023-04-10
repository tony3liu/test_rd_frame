# 测试套件-包含待测的模块、类、测试方法
# 测试加载器-决定测试模块、测试类、测试方法的加载
# 测试运行器-决定记录测试过程、输出测试结果

import unittest
import os

# 第一步：定义测试用例的路径
CASE_PATH = os.path.join(os.path.dirname(__file__), './unittest_case')

# 第二步：初始化创建将要用到的两个工具，测试套件和加载器
suit = unittest.TestSuite()
loader = unittest.defaultTestLoader

# 第三步：利用加载器中的扫描方法discover()去获取和加载测试用例路径下的测试用例对象
suit_content = loader.discover(start_dir=CASE_PATH, pattern='test_module*.py')

# 第四步：将加载器获取加载的测试用例添加进测试套件
suit.addTest(suit_content)

# 第五步：创建运行器,这里是文本运行器，为什么叫TextTestRunner，是因为这个运行器只能将测试结果以文本形式输出
# 类似的还有htmlTestRunner拓展组件的HtmlTestRunner()：网页运行器
runner = unittest.TextTestRunner()

# 第六步：运行器运行测试套件
runner.run(suit)
