# Define tool classes
import json
import time

from appium import webdriver as app_driver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _app_driver = None  # Define app driver

    # Define methods to modify private properties
    @classmethod
    def set_quit_driver(cls, mark):
        cls.__quit_mis_driver = mark

    # Obtain app driver
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_cap = {
                "platformName": "android",  # Choose Andriod platform
                "platformVersion": "5.1.1",  # Platform system version
                "deviceName": "****",  # Name of the device（If only one device can be replaced with ***）
                "appPackage": "hko.MyObservatory_v1_0",  # Name of app package
                "appActivity": "hko.homepage_v3.HomepageActivity",  # The page name of the app
                "noReset": True,  # It is used to remember the session of the app. If the value is True, no further operation is required.
                "resetKeyboard": True,  # Reset the keyboard of the device
                "unicodeKeyboard": True  # Input using Unicode encoding
            }
            cls._app_driver = app_driver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        return cls._app_driver

    # Defines method to exit the app driver
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None


# Encapsulate a method to select channels
def choice_channel(driver, element, channel):
    """
    :param driver:  App driver
    :param element:  Element
    :param channel:  The text content to select
    :return:
    """
    element.click()
    time.sleep(1)
    xpath = "//*[@class='android.widget.LinearLayout']//*[text()='{}']".format(channel)
    driver.find_element(By.XPATH, xpath).click()


# Encapsulate a method to determine whether an element exists
def is_exist(driver, text):
    """
    :param driver:  App driver
    :param text:   The text content of the element
    :return:
    """
    xpath = "//*[contains(text(), '{}')]".format(text)
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False


# Encapsulate a method to find element while swiping
def app_swipe_find(driver, element, target_ele):
    """
    :param driver: app driver
    :param element: The text content to swipe
    :param target_ele: The location's value of the element to be found
    :return:
    """
    location = element.location  # Gets the coordinate point position of the element
    x = location["x"]  # Gets the value of the coordinate point X
    y = location["y"]  # Gets the value of the coordinate point Y
    size = element.size
    width = size["width"]
    height = size["height"]
    start_x = x + width*0.5
    start_y = y + height * 0.9
    end_y = y + height * 0.1
    while True:
        page_source = driver.page_source
        try:
            time.sleep(1)
            driver.find_element(*target_ele).click()
            return True
        except Exception as e:
            driver.swipe(start_x, start_y, start_x, end_y, duration=1500)
        if page_source == driver.page_source:
            print("The screen has been scanned to the bottom, the corresponding channel is not found!")
            return False


# Encapsulate the method to obtain test data
def get_case_data(filename):
    """
    Sometimes we need data-driven test cases
    :param filename: The path and name of File
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
    list_case_data = []
    for case_data in case.values():
        list_case_data.append(tuple(case_data.values()))
    return list_case_data


