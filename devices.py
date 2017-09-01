import os
from appium import webdriver
from multiprocessing import Pool
import AppiumServer


class Device:
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        self.GET_VERSION = "adb shell getprop ro.build.version.release"

    def get_devices(self):
        value = os.popen(self.GET_ANDROID)
        # version = os.popen(self.GET_VERSION)

        # _version = version.readlines()[0].strip()

        devices = []

        for v in value.readlines():
            desired_caps = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.find('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = '5.0.1'
                desired_caps['deviceName'] = s_value[:s_value.find('device')]
                desired_caps['udid'] = s_value[:s_value.find('device')]
                desired_caps['appPackage'] = 'com.snailgame.cjg'
                desired_caps['appActivity'] = 'com.snailgame.cjg.MainActivity'
                # desired_caps['unicodeKeyboard'] = 'True'
                # desired_caps['resetKeyboard'] = 'True'

                devices.append(desired_caps)

        return devices


# def run_driver(_port, num):
#    a = Device()
#    b = a.get_devices()
#    driver = webdriver.Remote(str('http://localhost:%s/wd/hub') % _port, b[num])
#    driver.find_element_by_id('com.snailgame.cjg:id/tab_free_store').click()


# run_driver()

# a = Device()
# b = a.get_devices()
# print(b[0])
# print(b[1])
# driver = webdriver.Remote('http://localhost:4723/wd/hub', b[0])
# driver1 = webdriver.Remote('http://localhost:4725/wd/hub', b[1])

# if __name__ == '__main__':
#    port = 4723
#    p = Pool(2)
#    for i in range(2):
#        p.apply_async(run_driver, args=(port, i-1,))
#        port = port + 2
#    p.close()
#    p.join()

# if __name__ == '__main__':
#    a = Device().get_devices()
#    run = len(a)
#    test = AppiumServer.AppiumServer(run)
#    test.start_server()
#    test.kill_server()
