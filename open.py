# -*- coding: utf-8 -*-
from appium import webdriver
import time
import xlrd
import Decorator
import devices
import unittest
from HTMLTestRunner import HTMLTestRunner


# def decorator(func):
#    def wrapper(*args, **kwargs):
#        print('i am log')
#        return func(*args, **kwargs)
#    return wrapper

device = devices.Device()
desired_caps = device.get_devices()
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps[0])


def execl_rows(sheet):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(sheet)
    rows = index.nrows
    return rows


def read_excel(rowx, colx):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(0)
    value = index.cell_value(rowx, colx)
    return value


@Decorator.error_image
def login_test(x, y):
    driver.find_element_by_id('com.snailgame.cjg:id/iv_unlogin_avatar').click()
    time.sleep(1)
    driver.find_element_by_id('com.snailgame.cjg:id/common_login_btn').click()

    account = read_excel(x, y)
    print(account)
    driver.find_element_by_id('com.snailgame.cjg:id/account_input').send_keys(account)

    driver.find_element_by_id('com.snailgame.cjg:id/password_input').click()
    time.sleep(1)
    driver.press_keycode(29, 28672)
    driver.press_keycode(67)
    password = read_excel(x, y + 1)
    driver.find_element_by_id('com.snailgame.cjg:id/password_input').send_keys(password)
    driver.find_element_by_id('com.snailgame.cjg:id/login_button').click()
    time.sleep(5)
    ele = driver.find_element_by_name(u'会员')
    print(ele)
#   assert ele = True, 'error'

#    act = driver.current_activity
#
#    time.sleep(5)
#
#    print(act)
#    print(act1)
#
#    if act == act1:
#        source = driver.page_source
#        print(source)
#        print('pass')
#    else:
#        print('fail')
#        source = driver.page_source
#        print(source)
#        Decorator.screen(driver, 'login_test')
#        driver.find_element_by_id('com.snailgame.cjg:id/tv_title').click()
#        driver.find_element_by_id('com.snailgame.cjg:id/tv_title').click()
#        return -1


# @decorator
def logout_test():
    driver.find_element_by_id('com.snailgame.cjg:id/tv_right_action').click()
    driver.find_element_by_id('com.snailgame.cjg:id/sure').click()


# def screen_shot():
#    timestr = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#    img_name = timestr + '.png'
#    file = "D:\\test\\" + img_name
#    driver.get_screenshot_as_file(file)


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.1'
# desired_caps['deviceName'] = '3253ee99'
# desired_caps['appPackage'] = 'com.snailgame.cjg'
# desired_caps['appActivity'] = 'com.snailgame.cjg.MainActivity'
# desired_caps['unicodeKeyboard'] = 'True'
# desired_caps['resetKeyboard'] = 'True'



time.sleep(2)

driver.find_element_by_id('com.snailgame.cjg:id/mine').click()

act1 = driver.current_activity

time.sleep(2)

rows1 = execl_rows(0) - 1
while rows1 > 0:
    # login_test(rows1, 0)
    while login_test(rows1, 0) == -1:
        rows1 -= 1
    time.sleep(5)
    # screen_shot()
    # time.sleep(2)
    logout_test()
    time.sleep(2)
    rows1 -= 1

driver.close_app()
quit()
