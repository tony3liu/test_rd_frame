# 项目地址
# 项目包和文件夹路径
# 浏览器对象属性
# 测试套件
import os.path
from os.path import dirname, join

# ----------------------项目地址----------------------
# 项目1
PROJECT_ZENTAO_URL = "https://zentao.supremind.info/biz/user-login-L2Jpei9pbmRleC5odG1s.html"
# 项目2
PROJECT_CSDN_URL = ""
# ----------------------项目地址----------------------


# ----------------------项目包和文件夹路径----------------------
# 项目根目录
BASE_PATH = dirname(__file__)
# 浏览器驱动目录
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, "browser_drivers/chromedriver")
# 项目模块的路径
BASE_MODULE_PATH = os.path.join(BASE_PATH, "base")
UNITTEST_CASE_MODULE_PATH = os.path.join(BASE_PATH, "unittest_case")
REPORT_PATH = os.path.join(BASE_PATH, "reports")
# ----------------------项目包和文件夹路径----------------------


# ----------------------浏览器对象属性----------------------
# 浏览器基本属性
# 默认窗口尺寸
WIN_SIZE = (1024, 768)
# 默认隐式等待时间
IMP_TIME = 30
# 默认页面加载时间
PAGE_LOAD_TIME = 20
# 默认JS异步执行时间
SCRIPT_TIME_OUT = 20
# 默认使用无头浏览器
HEADLESS = True

# 浏览器特有属性
# Chrome
OPTION_MARK = True  # 开关: 用于控制options方法的执行结果
BROWSER_MARK = True  # 开关: 用于控制browsers方法的执行结果
CLEAN_SESSION = True
START_MAX = '--start-maximized'
EXP = {
        'excludeSwitches': ['enable-automation'],  # 不显示"chrome正受到自动化软件控制"的提示
        # 'mobileEmulation': {'deviceName': 'iphone 12'}  # 以移动端iPhone 12显示web，一般不加
    }
# ----------------------浏览器对象属性----------------------


# ----------------------测试套件----------------------
# 流程1相关的测试套件
SUIT_MODULE_1 = ['test_module_1.py', 'test_module_2.py']
# 流程2相关的测试套件
SUIT_MODULE_2 = ['test_module_3.py', 'test_module_4.py']

# 主测试套件
# 项目1 的套件
SUIT_PROJECT_1 = SUIT_MODULE_1 + SUIT_MODULE_2
# 项目2 的套件
SUIT_PROJECT_2 = SUIT_MODULE_1
# ----------------------测试套件----------------------

