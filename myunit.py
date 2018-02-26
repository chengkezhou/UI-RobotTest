from test_case.models.driver import web_chrome,web_pjs
from test_case.models.function import saas_par
import unittest,time
import psycopg2

# 测试参数（读表）
url_par_1 = saas_par(0,4,2)
user_par_1 = saas_par(0,4,4).split(',',1)

# 定位元素（读表）
login_ele_1 = saas_par(1,4,2)
login_ele_2 = saas_par(1,4,3)
login_ele_3 = saas_par(1,4,4)
login_ele_4 = saas_par(1,4,5)
login_ele_5 = saas_par(1,4,6)
login_ele_6 = saas_par(1,4,7)

# 断言（读表）
login_ass_1 = saas_par(1,9,7)

class MyTest1(unittest.TestCase):
    '''
        setUP：
            打开浏览器
        tearDown：
            关闭浏览器
    '''

    def setUp(self):
        self.driver = web_chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()


class MyTest2(unittest.TestCase):
    '''
        setUP：
            打开浏览器
            登录
        tearDown：
            关闭浏览器
    '''

    def setUp(self):
        # 打开浏览器
        self.driver = web_chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # 登录
        driver = self.driver
        driver.get(url_par_1)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(login_ele_1).clear()
        driver.find_element_by_xpath(login_ele_1).send_keys(user_par_1[0])
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(login_ele_2).clear()
        driver.find_element_by_xpath(login_ele_2).send_keys(user_par_1[1])
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//form//button').click()
        time.sleep(1)

        # 滚动到最底部
        target = self.driver.find_element_by_xpath(login_ele_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        # 同意协议
        self.driver.find_element_by_xpath(login_ele_5).click()
        self.driver.implicitly_wait(10)

        # 验证是否登录成功
        logintext = self.driver.find_element_by_xpath(login_ele_6).text
        self.assertEqual(logintext, login_ass_1)
        print('login success ! ')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()






