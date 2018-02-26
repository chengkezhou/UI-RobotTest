from selenium.webdriver import Remote
from selenium import webdriver

# 启动浏览器驱动
def web_chrome():
    driver = webdriver.Chrome()
    # host = '127.0.0.1:4444'     # 运行主机：端口号（本机默认：127.0.0.1：4444）
    # dc = {'browserName':'firefox'}      # 指定浏览器
    # driver= Remote(command_executor="http://"+host+"/wd/hub")
    return driver

def web_pjs():
    driver = webdriver.PhantomJS()
    return driver

if __name__=='__main__':
    dr = web_chrome()
    dr.get('http://www.baidu.com')
    dr.quit()

