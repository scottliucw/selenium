import xlrd
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header


def send_email():
    to_list = ['liucw@snail.com']
    from_mail = 'szyjpx@163.com'
    host_dir = 'smtp.163.com'
    username = 'szyjpx@163.com'
    password = '102581LCW'

    message = MIMEText(u'测试完成', 'plain', 'utf-8')
    message['from'] = Header("szyjpx@163.com", 'utf-8')
    message['To'] = Header("liucw@snail.com", 'utf-8')
    message['Subject'] = Header('Python email test', 'utf-8')

    e = smtplib.SMTP()
    e.connect(host_dir, port=25)
    e.login(username, password)
    e.sendmail(from_mail, to_list, message.as_string())

    e.quit()

    print('send email')

if __name__ == '__main__':
    send_email()
