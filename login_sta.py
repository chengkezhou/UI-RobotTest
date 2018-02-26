import unittest
from test_case.models import myunit
from test_case.models.function import saas_par
import time
# from test_case.parameter.element_par import *
# from test_case.parameter.test_par import *
# from test_case.parameter.assert_par import *

# 测试参数（读表）
url_par_1 = saas_par(0,4,2)
user_par_1 = saas_par(0,4,4).split(',',1)
user_par_2 = saas_par(0,4,5).split(',',1)
user_par_3 = saas_par(0,4,6).split(',',1)
user_par_4 = saas_par(0,4,7).split(',',1)
user_par_5 = saas_par(0,4,8).split(',',1)
user_par_6 = saas_par(0,4,9).split(',',1)
user_par_7 = saas_par(0,4,10).split(',',1)
user_par_8 = saas_par(0,4,11).split(',',1)
user_par_9 = saas_par(0,4,12).split(',',1)
user_par_10 = saas_par(0,4,13).split(',',1)


# 定位元素（读表）
login_ele_1 = saas_par(1,4,2)
login_ele_2 = saas_par(1,4,3)
login_ele_3 = saas_par(1,4,4)
login_ele_4 = saas_par(1,4,5)
login_ele_5 = saas_par(1,4,6)
login_ele_6 = saas_par(1,4,7)
login_ele_7 = saas_par(1,4,8)
login_ele_8 = saas_par(1,4,9)
login_ele_9 = saas_par(1,4,10)
login_ele_10 = saas_par(1,4,11)

# 断言（读表）
login_ass_1 = saas_par(1,9,7)
login_ass_2 = saas_par(1,9,8)
login_ass_3 = saas_par(1,9,9)
logout_ass_1 = saas_par(1,9,4)


class LoginTest(myunit.MyTest1):
    '''登录'''

    def login(self,user,psw):
        '''登录方法'''
        driver = self.driver
        driver.get(url_par_1)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(login_ele_1).clear()
        driver.find_element_by_xpath(login_ele_1).send_keys(user)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(login_ele_2).clear()
        driver.find_element_by_xpath(login_ele_2).send_keys(psw)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(login_ele_3).click()
        time.sleep(2)
        # driver.implicitly_wait(10)

    def test_login01(self,n=0):
        '''正常登录'''
        try:
            self.login(user_par_1[0],user_par_1[1])

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
        except Exception as msg:
            # 因未找到元素而产生的异常，对此用例进行2次重试
            if ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login01(n)
            raise

    def test_login02(self, n=0):
        '''账号为空'''
        try:
            self.login(user_par_2[0], user_par_2[1])
            login_usernull = self.driver.find_element_by_xpath(login_ele_7).text
            self.assertEqual(login_usernull,login_ass_2)
            print('login fail ! ')
        except Exception as msg:
            if ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login02(n)
            raise

    def test_login03(self, n=0):
        '''密码为空'''
        try:
            self.login(user_par_3[0], user_par_3[1])
            login_pswnull = self.driver.find_element_by_xpath(login_ele_8).text
            self.assertEqual(login_pswnull,login_ass_3)
            print('login fail ! ')
        except Exception as msg:
            if ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login03(n)
            raise

    def test_login04(self, n=0):
        '''账号密码都为空'''
        try:
            self.login(user_par_4[0], user_par_4[1])
            login_usernull = self.driver.find_element_by_xpath(login_ele_7).text
            self.assertEqual(login_usernull,login_ass_2)
            login_pswnull = self.driver.find_element_by_xpath(login_ele_8).text
            self.assertEqual(login_pswnull,login_ass_3)
            print('login fail ! ')
        except Exception as msg:
            if ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login04(n)
            raise

    def test_login05(self, n=0):
        '''账号错误'''
        try:
            self.login(user_par_5[0], user_par_5[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login06(self, n=0):
        '''密码错误'''
        try:
            self.login(user_par_6[0], user_par_6[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login07(self, n=0):
        '''账号大小写不匹配'''
        try:
            self.login(user_par_7[0], user_par_7[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login08(self, n=0):
        '''密码大小写不匹配'''
        try:
            self.login(user_par_8[0], user_par_8[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login09(self, n=0):
        '''账号输入非法字符'''
        try:
            self.login(user_par_9[0], user_par_9[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login10(self, n=0):
        '''密码输入非法字符'''
        try:
            self.login(user_par_10[0], user_par_10[1])
            self.driver.find_element_by_xpath(login_ele_5)
        except Exception as msg:
            if login_ele_5 in str(msg):
                print('login fail ! ')
            elif ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_login10(n)
                raise

    def test_login11(self,n=0):
        '''账号输入长度超限'''
        pass

    def test_login12(self,n=0):
        '''密码输入长度超限'''
        pass

if __name__ == '__main__':
    unittest.main()

