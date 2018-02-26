import unittest,time
from test_case.models import myunit
from test_case.models.function import saas_par


class MuneButton(myunit.MyTest2):
    '''各级菜单按钮'''

    def test_mune_01(self,n=0):
        '''数据服务-缩放按钮'''
        # 点击【<<】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/button/span/i').click()
        time.sleep(1)
        # 断言【车辆】text不可见
        text1 = self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/div/span').text
        self.assertIsNotNone(text1)
        # 点击【>>】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/button/span/i').click()
        time.sleep(1)
        # 断言【车辆】text='车辆'
        text2 = self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/div/span').text
        self.assertEqual(text2,'车辆')

    def test_mune_02(self,n=0):
        '''数据服务-车辆-车辆列表'''
        # 点击【车辆列表】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/ul/li[1]').click()
        self.driver.implicitly_wait(10)
        # 断言【车辆列表】text='车辆列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'车辆列表')

    def test_mune_03(self,n=0):
        '''数据服务-行程日志-事件'''
        # 点击【事件】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[2]/ul/li[1]').click()
        self.driver.implicitly_wait(10)
        # 断言【事件列表】text='事件列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'事件列表')

    def test_mune_04(self,n=0):
        '''数据服务-行程日志-紧急'''
        # 点击【紧急】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[2]/ul/li[2]').click()
        self.driver.implicitly_wait(10)
        # 断言【紧急事件】text='紧急列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'紧急列表')

    def test_mune_05(self,n=0):
        '''数据服务-行程日志-数据'''
        # 点击【数据】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[2]/ul/li[3]').click()
        self.driver.implicitly_wait(10)
        # 断言【数据列表】text='数据列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'数据列表')

    def test_mune_06(self,n=0):
        '''数据服务-统计-基本'''
        # 点击【基本】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[3]/ul/li[1]').click()
        self.driver.implicitly_wait(10)
        # 断言【基本统计】text='基本统计'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'基本统计')

    def test_mune_07(self,n=0):
        '''数据服务-统计-设备'''
        # 点击【设备】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[3]/ul/li[2]').click()
        self.driver.implicitly_wait(10)
        # 断言【设备统计】text='设备统计'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'设备统计')

    def test_mune_08(self,n=0):
        '''管理控制台'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 断言【管理控制台】text='管理控制台'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[1]/span').text
        self.assertEqual(text,'管理控制台')

    def test_mune_09(self, n=0):
        '''管理控制台-缩放按钮'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【<<】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/button/span/i').click()
        time.sleep(1)
        # 断言【设备】text不可见
        text1 = self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/div/span').text
        self.assertIsNotNone(text1)
        # 点击【>>】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/button/span/i').click()
        time.sleep(1)
        # 断言【设备】text='设备'
        text2 = self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/div/span').text
        self.assertEqual(text2,'设备')


    def test_mune_10(self,n=0):
        '''管理控制台-设备-设备列表'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【设备列表】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/ul/li[1]').click()
        self.driver.implicitly_wait(10)
        # 断言【设备列表】text='设备列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'设备列表')

    def test_mune_11(self,n=0):
        '''管理控制台-设备-电子围栏'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【电子围栏】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[1]/ul/li[2]').click()
        self.driver.implicitly_wait(10)
        # 断言【电子围栏】text='电子围栏'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'电子围栏')


    def test_mune_12(self,n=0):
        '''管理控制台-设备-车辆列表'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【车辆列表】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[2]/ul/li').click()
        self.driver.implicitly_wait(10)
        # 断言【车辆列表】text='车辆列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'车辆列表')


    def test_mune_13(self,n=0):
        '''管理控制台-用户-账号'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【账号】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[3]/ul/li[1]').click()
        self.driver.implicitly_wait(10)
        # 断言【账号列表】text='账号列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'账号列表')


    def test_mune_14(self,n=0):
        '''管理控制台-用户-公司'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【公司】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[3]/ul/li[2]').click()
        self.driver.implicitly_wait(10)
        # 断言【公司列表】text='公司列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'公司列表')


    def test_mune_15(self,n=0):
        '''管理控制台-用户-角色'''
        # 点击【管理控制台】
        self.driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]').click()
        time.sleep(1)
        # 点击【角色】
        self.driver.find_element_by_xpath('//*[@id="aside-menu"]/li[3]/ul/li[3]').click()
        self.driver.implicitly_wait(10)
        # 断言【角色列表】text='角色列表'
        text = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div[1]/div/span[2]/span').text
        self.assertEqual(text,'角色列表')



if __name__ == '__main__':
    unittest.main()

