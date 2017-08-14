#!/usr/bin/env python
# encoding: utf-8

import HTMLTestRunner
import time
import unittest
import myclass


def decorator(func):
    def wrapper(*args, **kwargs):
        print('i am log')
        return func(*args, **kwargs)
    return wrapper


class mytest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        pass

        # 退出清理工作

    def tearDown(self):
        pass

        # 具体的测试用例，一定要以test开头

    @decorator
    def test_sum(self):
        self.assertEqual(myclass.sum(1, 2), 0, 'test sum fail')

    def test_sub(self):
        self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(mytest("test_sum"))
    # testunit.addTest(mytest("test_sub"))
    HtmlFile = "D:\\test\\" + now + "HTMLtemplate.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
    runner.run(testunit)

    fp.close()
