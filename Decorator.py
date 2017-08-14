import time
from functools import wraps
import BasePage
import logging

logging.basicConfig(level=logging.INFO)


def screen(file_name):
    timestr = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    img_name = file_name + '-' + timestr + '.png'
    img_path = "D:\\test\\" + img_name
    driver = BasePage.BasePage().get_driver()
    driver.get_screenshot_as_file(img_path)


def error_image(func):
    #    def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('decorator is running')
            func(*args, **kwargs)
        except Exception:
            #               screen(driver, func.__name__)
            screen(func.__name__)
            raise
        else:
            logging.info("%s 脚本运行正常" % func.__name__)
    return wrapper

#    return decorator
