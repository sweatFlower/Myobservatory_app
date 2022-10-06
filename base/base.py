# Difine the app base class
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


# Encapsulate the object library level of base class
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_app_driver()  # Obtain the app driver

    def get_element(self, location):
        """

        :param location: The location's value of the element to be found
        :return:
        """
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element

    def get_elements(self, location):
        """

        :param location: The location's value of the element to be found
        :return:
        """
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_elements(*location))
        return element


# Encapsulate the operational level of base class
class BaseHandle:
    pass
