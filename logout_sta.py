import unittest,time
from test_case.models import myunit
from test_case.models.function import saas_par

# 定位元素（读表）
logout_ele_1 = saas_par(1,4,10)
logout_ele_2 = saas_par(1,4,11)
login_ele_3 = saas_par(1,4,4)

# 断言（读表）
logout_ass_1 = saas_par(1,9,4)

class LogoutTest(myunit.MyTest2):
    '''注销'''

    def logout(self):
        '''注销方法'''
        self.driver.find_element_by_xpath(logout_ele_1).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(logout_ele_2).click()
        self.driver.implicitly_wait(10)

    def test_logout(self,n=0):
        '''注销登录'''
        try:
            self.logout()
            logouttext = self.driver.find_element_by_xpath(login_ele_3).text
            self.assertEqual(logout_ass_1,logouttext)
            print('log out !')
        except Exception as msg:
            if ('no such element' in str(msg)) and n < 2:
                n += 1
                self.test_logout(n)
            raise


if __name__ == '__main__':
    unittest.main()
