# The objects of page "9-Day Forecast"
# Encapsulate the object library
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


class ForecastPage(BasePage):
    def __init__(self):
        super().__init__()
        # Date
        self.date = By.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_date"
        # Temperature
        self.temperature = By.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_temp"
        # Humidity
        self.humidity = By.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_rh"
        # Ultraviolet
        self.ultraviolet = By.ID, "hko.MyObservatory_v1_0:id/psrText"
        # Wind
        self.wind = By.ID, "hko.MyObservatory_v1_0:id/psrText"
        # Details
        self.detail = By.ID, "hko.MyObservatory_v1_0:id/sevenday_forecast_details"

    # Find date
    def find_date(self,num):
        return self.get_elements(self.date)[num]

    # Find temperature
    def find_temperature(self):
        return self.get_element(self.temperature)

    # Find humidity
    def find_humidity(self,num):
        return self.get_elements(self.humidity)[num]

    # Find ultraviolet
    def find_ultraviolet(self,num):
        return self.get_elements(self.ultraviolet)[num]

    # Find wind
    def find_wind(self,num):
        return self.get_elements(self.wind)[num]

    # Find detail
    def find_detail(self,num):
        return self.get_elements(self.detail)[num]


# Encapsulate the operational level
class ForecastHandle(BaseHandle):
    def __init__(self):
        self.forecast_page = ForecastPage()

    # Print date
    def print_date(self,num):
        self.forecast_page.find_date(num).click

    # Print temperature
    def print_temperature(self,num):
        self.forecast_page.find_temperature(num).click

    # Print humidity
    def print_humidity(self,num):
        self.forecast_page.find_humidity(num).click

    # Print ultraviolet
    def print_ultraviolet(self,num):
        self.forecast_page.find_ultraviolet(num).click

    # Print wind
    def print_wind(self,num):
        self.forecast_page.find_wind(num).click

    # Print detail
    def print_detail(self,num):
        self.forecast_page.find_detail(num).click


# Encapsulate the business level
class ForecastProxy:
    def __init__(self):
        self.forecast_handle = ForecastHandle()

    # Check tomorrow weacher
    def print_weather(self, num):
        self.forecast_handle.print_date(num)
        self.forecast_handle.print_temperature(num)
        self.forecast_handle.print_humidity(num)
        self.forecast_handle.print_ultraviolet(num)
        self.forecast_handle.print_wind(num)
        self.forecast_handle.print_detail(num)

