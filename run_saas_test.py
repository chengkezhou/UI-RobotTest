#!/usr/bin/python3

import unittest
import HTMLTestRunner
import time
from test_case.models.function import new_report,send_mail

if __name__=="__main__":
    test_report = 'C:\\Users\\12114\\Desktop\\SaasTest\\result'
    now =str(time.strftime("%Y-%m-%d %H_%M_%S"))
    filename = "C:\\Users\\12114\\Desktop\\SaasTest\\result\\"+now+"report.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='SaaS平台测试报告',description='环境：windows 10    浏览器：Chrome')

    discover = unittest.defaultTestLoader.discover('C:\\Users\\12114\\Desktop\\SaasTest\\test_case',pattern='*_sta.py')
    runner.run(discover)

    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)
