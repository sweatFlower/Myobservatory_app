# Define test classes
import pytest
import allure

from page.index_page import IndexProxy
from page.weather_forecast import ForecastProxy
from utils import UtilsDriver, is_exist


@pytest.mark.run(order=1)
class TestTomorrowWeather:
    # Define a class-level fixture initialization method
    def setup_class(self):
        self.indxe_proxy = IndexProxy()
        self.forecast_proxy = ForecastProxy()

    # Define a class-level fixture destruction method
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    # Define test methods
    @allure.story("Check tomorrow weather")
    @pytest.mark.parametrize("check_date, weather_number", [("4 Oct", 0)])
    def test_tomorrow_weather(self, check_date, weather_number):
        self.indxe_proxy.find_channel("9-Day Forecast")
        # Input the date I want to check
        assert is_exist(UtilsDriver.get_app_driver(), check_date)
        # Input the number of the weather I want to check
        self.forecast_proxy.print_weather(weather_number)

