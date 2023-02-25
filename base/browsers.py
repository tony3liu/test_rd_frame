# coding: utf-8
# 浏览器的类型（Chrome, ie, firefox, edge, opera）
# 浏览器的启动参数（无头化, 最大化, 尺寸化）
# 浏览器的属性（显示尺寸, 隐式等待, 页面加载, JS执行时间）
from typing import Type, Union
from selenium.webdriver import *


# 定义异常类，供异常处理使用
class BrowsersTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f"unsupported Browser Type:{self._type}"


class OptionsTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f"unsupported Option Type:{self._type}"


class BROWSER:
    # 浏览器驱动路径
    CHROME_DRIVER_PATH = "../browser_drivers/chromedriver"
    FIREFOX_DRIVER_PATH = ""
    IE_DRIVER_PATH = ""
    EDGE_DRIVER_PATH = ""
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

    def __init__(self, browser_type: Type[Union[Firefox, Chrome, Ie, Edge]] = Chrome,
                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        # 先对参数做异常处理
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Edge)):
            raise BrowsersTypeError(browser_type)
        if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
            raise OptionsTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError

        self._path = driver_path
        self._browser = browser_type  # 浏览器的实例化
        self._option = option_type  # 浏览器的启动参数

    @property
    def options(self):
        """
        浏览器的特定操作，在子类中实现
        :param self:
        :return:
        """
        return

    @property
    def browsers(self):
        """
        启动浏览器，返回浏览器的实例,具体也要在子类中定制化实现
        :return:
        """
        return


class CHROME(BROWSER):
    OPTION_MARK = True  # 开关: 用于控制options方法的执行结果

    BROWSER_MARK = True  # 开关: 用于控制browsers方法的执行结果

    HEADLESS = False

    CLEAN_SESSION = True

    IMP_TIME = 30

    PAGE_LOAD_TIME = 30

    SCRIPT_TIME_OUT = 30

    WIN_SIZE = (1920, 900)

    START_MAX = '--start-maximized'

    EXP = {
        'excludeSwitches': ['enable-automation'],  # 不显示"chrome正受到自动化软件控制"的提示
        # 'mobileEmulation': {'deviceName': 'iphone 12'}  # 以移动端iPhone 12显示web，一般不加
    }

    @property
    def options(self):
        if self.OPTION_MARK:
            # 这里特别注意，self._option是Chrome的Option类，这个方法里面要配置chrome，所以先获取Option实例，然后调用Option实例的方法来配置chrome
            chrome_options = self._option()
            # 将定义的启动参数加入Chrome浏览器启动参数中
            chrome_options.add_argument(self.START_MAX)
            # 清理缓存要调用专用的ensure_clean_session方法
            chrome_options.ensure_clean_session = self.CLEAN_SESSION
            # 将EXP中的键值对参数加入Chrome浏览器启动参数中
            for k, v in self.EXP.items():
                chrome_options.add_experimental_option(k, v)
            chrome_options.headless = self.HEADLESS
            return chrome_options
        return None  # 如果开关为False，就会返回None

    @property
    def browsers(self):
        if self.BROWSER_MARK:
            # 实例化chrome浏览器，通过driver_path和启动项options方法启动浏览器
            chrome = self._browser(self._path, options=self.options)
            # 将浏览器的相关参数引入成类的配置项，使配置项生效
            chrome.implicitly_wait(self.IMP_TIME)
            # chrome.set_window_size(*self.WIN_SIZE)  # 一般可以不用设置这个窗口大小
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
            return chrome  # 将封装改造好的浏览器对象返回出来，供封装页面时直接调用
        return None  # 如果开关为False，就会返回None


class IE(BROWSER):
    OPTION_MARK = True  # 开关: 用于控制options方法的执行结果

    BROWSER_MARK = True  # 开关: 用于控制browsers方法的执行结果

    CLEAN_SESSION = True

    def __init__(self):
        # 用super(subclass, self)方法调用父类的方法并重写该方法
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH
        )

    @property
    def options(self):
        if self.OPTION_MARK:
            ie_options = self._option()
            ie_options.ensure_clean_session = self.CLEAN_SESSION
            return ie_options
        return None

    @property
    def browsers(self):
        if self.BROWSER_MARK:
            ie = self._browser(self._path, options=self.options)
            ie.set_script_timeout(self.SCRIPT_TIME_OUT)
            ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
            ie.implicitly_wait(self.IMP_TIME)
            return ie
        return None
