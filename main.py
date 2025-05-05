import pages
import data
import time
import helpers
import localizadores
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestUrbanRoutes:

    driver = None

    @classmethod

    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.urban_routes_page = pages.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.urban_routes_page.set_route(address_from, address_to)
        assert self.urban_routes_page.get_from() == address_from
        assert self.urban_routes_page.get_to() == address_to


    def test_select_comfort(self):
        self.urban_routes_page.click_order_a_taxi_button()
        self.urban_routes_page.click_fare_comfort()
        icecream_visible=self.driver.find_element(*localizadores.UrbanRoutesPage.order_icecream)
        assert icecream_visible.is_displayed(), "comfort"

    def test_number_phone(self):
        self.urban_routes_page.set_phone()
        assert self.urban_routes_page.get_phone() == data.phone_number

    def test_card_credit(self):
        self.urban_routes_page.click_next_button()
        self.urban_routes_page.code_number()
        self.urban_routes_page.send_cell_info()
        self.urban_routes_page.click_card()
        self.urban_routes_page.add_card()
        self.urban_routes_page.close_window()
        assert self.urban_routes_page.get_card_input() == data.card_number
        assert self.urban_routes_page.get_cvv_card() == data.card_code

    def test_message_drive(self):
        message = data.message_for_driver
        self.urban_routes_page.write_drive_message(message)
        assert self.urban_routes_page.get_message() == data.message_for_driver

    def test_blankets_scarves(self):
        self.urban_routes_page.request_blanket_and_scarves()
        assert self.urban_routes_page.get_blanket_and_scarves() == self.urban_routes_page.request_blanket_and_scarves()

    def test_icecream(self):
        self.urban_routes_page.request_ice_cream()
        assert self.urban_routes_page.get_ice_cream() == self.urban_routes_page.request_ice_cream()

    def test_taxi(self):
        self.urban_routes_page.order_taxi()
        order_taxi_visible=self.driver.find_element(*localizadores.UrbanRoutesPage.modal_taxi)
        assert order_taxi_visible.is_displayed(), "Muéstrame el camino"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

