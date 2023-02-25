# 页面实例化
# 页面属性封装（URL, 浏览器实例, 元素, 操作）
# 页面调用（页面继承， 页面实例化）
# 基于页面调用可以有两种方式
from base.browsers import *


# 页面实例化，需要将页面元素定义定位器
class Page:
    url = None
    # 这里设计这个定位器locators，就要结合selenium中的find_element方法的参数特性
    # 要有by,value两个参数,所以这个字典形式是这样{key1:(by,value),key2:(by,value)}
    locators = {}
    browser = CHROME

    def __init__(self, page=None):
        """
        定义page基类的构造方法
        在构造方法中实现浏览器的启动
        和页面继承时，获得浏览器实例
        """
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browsers

    def __getattr__(self, loc):
        # 用getattr方法来处理调用类不存在的属性时会抛的异常，getattr会动态创建这个不存在的属性从而避免抛异常
        # 这里利用getattr会动态创建属性的特性，来动态绑定页面实例的属性，这个属性就对应定位器locator中元素的key
        if loc not in self.locators.keys():
            raise Exception
        by, val = self.locators[loc]
        return self.driver.find_element(by, val)


# 创建公用页面（登录）
class CommonLoginPage(Page):
    url = "https://zentao.supremind.info/biz/user-login-L2Jpei9pbmRleC5odG1s.html"
    locators = {
        'username': ('id', 'account'),
        'password': ('name', 'password'),
        'submit_button': ('id', 'submit')
    }

    # 定义打开网页和登录的操作
    def get(self):
        self.driver.get(self.url)

    def login(self, username: str = 'liutao', password: str = 'smAI2021'):
        """
        上面基类的getattr函数就在这里发挥作用，
        将定位器locator中的键通过页面实例直接调用，
        这些locator就会绑定到页面实例上，成为页面的属性
        并且已经成了执行过find element的对象
        :param username:
        :param password:
        """
        self.username.sendkeys(username)
        self.password.sendkeys(password)
        self.submit_button.click()


# 创建具体的业务页面
class MainPage(CommonLoginPage):
    # 将定位器更新，update方法会将新的定位 k:v 元素加进locators

    CommonLoginPage.locators.update(
        {
            'search_input_bug_id': ('id', 'searchInput'),
            'search_go_button': ('id', 'searchGo'),
            'user_name': ('xpath', ''),
            'bug_label': ('xpath', ''),
            'login_out_button': ('xpath', '//a[text()=="退出"]')
        }
    )

# 下面都是具体自动化测试的case方法的举例，根据需要自己编写,需要用到的定位元素，更新进locators
    def search_bug(self, bug_id: str = '1359'):
        self.search_input_bug_id.sendkeys(bug_id)
        self.search_go_button.click()

    def login_out(self):
        self.user_name.click()
        self.login_out_button.click()