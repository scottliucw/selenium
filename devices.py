import os
from appium import webdriver


class Device:
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        self.GET_VERSION = "adb shell getprop ro.build.version.release"

    def get_devices(self):
        value = os.popen(self.GET_ANDROID)
        version = os.popen(self.GET_VERSION)

        _version = version.readlines()[0].strip()

        devices = []

        for v in value.readlines():
            desired_caps = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.find('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = _version
                desired_caps['deviceName'] = s_value[:s_value.find('device')]
                desired_caps['appPackage'] = 'com.snailgame.cjg'
                desired_caps['appActivity'] = 'com.snailgame.cjg.MainActivity'
                desired_caps['unicodeKeyboard'] = 'True'
                desired_caps['resetKeyboard'] = 'True'

                devices.append(desired_caps)

        return devices

# a = Device()
# b = a.get_devices()
# print(b[0])
# driver = webdriver.Remote('http://localhost:4723/wd/hub', b[0])
