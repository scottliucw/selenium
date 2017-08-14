import devices
import BasePage
from appium import webdriver
import unittest
import testcase
import time
import HTMLTestRunner


def main():
    dev = devices.Device().get_devices()

    if not len(dev):
        print('there is no device connected this PC')
        return

    driver = webdriver.Remote('http://localhost:4723/wd/hub', dev[0])
    base_page = BasePage.BasePage()
    base_page.set_driver(driver)

    testunit = unittest.TestSuite()
    testunit.addTests(map(testcase.freestore, ["test_login_logout", "test_mian"]))
    # testunit.addTest(testcase.freestore("test_mian"))
    # test_suit.addTests(map(Mydemo, ["Mytest1", "Mytest2", "Mytest3"]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "D:\\test\\" + now + "HTMLtemplate.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
    runner.run(testunit)

    fp.close()

if __name__ == '__main__':
    main()
