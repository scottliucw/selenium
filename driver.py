from multiprocessing import Process
from multiprocessing import Pool
import os
import Ports
import sys
import devices
from appium import webdriver
import runcase
import AppiumServer
import BasePage


class Driver:
    @staticmethod
    def _run_cases(run):
        driver = webdriver.Remote(str('http://localhost:%s/wd/hub') % run.get_port()[0], run.get_device())

        base_page = BasePage.BasePage()
        base_page.set_driver(driver)

        # run.run(cases)
        driver.find_element_by_id('com.snailgame.cjg:id/tab_free_store').click()
        driver.quit()

    def run_driver(self):
        device = devices.Device().get_devices()
        port = Ports.Ports().get_ports(len(device))

        if not len(device):
            print('测试设备未连接！')
            return

        runs = []
        for i in range(len(device)):
            runs.append(runcase.RunCase(device[i], port[i]))

        Appium_server = AppiumServer.AppiumServer(runs)
        Appium_server.start_server()
        print('good')

        pool = Pool(processes=len(runs))
        for run in runs:
            print('hello')
            pool.apply_async(self._run_cases, args=(run,))
        pool.close()
        pool.join()


if __name__ == '__main__':
    a = Driver()
    a.run_driver()
