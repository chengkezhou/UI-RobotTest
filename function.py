from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
import time
import smtplib
import os
import xlrd
import psycopg2

# 截图函数
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)

# 发送带测试报告的邮件
def send_mail(file_new):
    smtpserver = 'smtp.huabaotech.com'  # 发件服务器
    sender = 'noreply@huabaotech.com'   # 发件人及账号
    password = 'Abc'     # 发件账号密码

    receiver = ['zhouchengke@huabaotech.com','mars.zhu@huabaotech.com','jun.hu@huabaotech.com','edward@huabaotech.com','hufang@huabaotech.com']      # 收件人账号
    # receiver = ['zhouchengke@huabaotech.com','121142125@qq.com','731015454@qq.com','631733025@qq.com']
    # receiver = ['zhouchengke@huabaotech.com']

    f = open(file_new,'rb')
    mail_body = f.read()    # 获取new_report返回的heml作为邮件内容的变量
    f.close()

    now = str(time.strftime("%Y-%m-%d %H:%M:%S"))
    msg = MIMEMultipart()
    puretext = MIMEText(mail_body,'html','utf-8')    # html邮件内容
    msg.attach(puretext)
    xlsxpart = MIMEApplication(open(file_new, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='report%s.html'%now)
    msg.attach(xlsxpart)
    msg['Subject'] = Header('自动化测试报告 %s'%now,'utf-8')  # 邮件标题
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)

    smtp = smtplib.SMTP_SSL()
    smtp .connect(smtpserver,465)    # 连接发信服务器
    smtp.login(sender,password)   # 设置发信账号
    smtp.sendmail(
        sender, # 发信邮箱
        receiver,   # 收信邮箱
        msg.as_string())
    smtp.quit()
    print('email has send out !')

# 获取最新的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

# 从参数表格中读取数据
def saas_par(n1=0,n2=0,n3=0):
    xls = xlrd.open_workbook('C:\\Users\\12114\\Desktop\\SaasTest\\saas_par.xlsx')
    sheet = xls.sheets()[n1]
    col = sheet.col_values(n2)[n3]
    return col

a=saas_par(0,4,2)
print(a)



# if __name__ == '__main__':
#     send_mail(new_report('C:\\Users\\12114\\Desktop\\SaasTest\\result'))
