# The objects of index page
# Encapsulate the object library
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle
from utils import app_swipe_find


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # The menu key on the left
        self.left_menu = By.CLASS_NAME, "android.widget.ImageButton"
        # The slide list
        self.slideable_listview = By.ID, "hko.MyObservatory_v1_0:id/left_drawer"
        # Channel to click on
        self.channel = By.XPATH, "//*[contains(@text, '{}')]"

    # Find the menu key on the left
    def find_left_menu(self):
        return self.get_element(self.left_menu)

    # find the slide list
    def find_slideable_listview(self):
        return self.get_element(self.slideable_listview)


# Encapsulate the operational level
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()

    # Click the menu key on the left
    def click_left_menu(self):
        self.index_page.find_left_menu().click

    # Finding the channel while swiping
    def click_channel(self, channel):
        xpath = self.index_page.channel[0], self.index_page.channel[1].format(channel)
        app_swipe_find(self.index_page.driver, self.index_page.find_slideable_listview(), xpath)


# Encapsulate the business level
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # Go to page "9-day-forecast"
    def find_channel(self, channel):
        self.index_handle.click_left_menu()
        self.index_handle.click_channel(channel)
