import time
from time import sleep

from selenium import webdriver
from selector import UrbanRoutesPage
import data


class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    # ----- Funciones que agrupan pasos a seguir de los test -----
    def set_up_base_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.select_taxi_button()
    def set_up_base_comfort(self):
        self.set_up_base_route()
        self.routes_page.select_comfort_rate()
    def set_up_before_driver_modal(self):
        self.set_up_base_comfort()
        self.routes_page.request_blanket_and_tissues()
        self.routes_page.request_ice_cream()
        self.routes_page.search_taxi()

    # ----- Tests individuales (con assert propio en cada uno) -----
    def test_01_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_02_select_comfort_rate(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.select_taxi_button()
        self.routes_page.select_comfort_rate()
        assert self.routes_page.comfort_button # Este método debes implementarlo

    def test_03_fill_phone_number(self):
        self.set_up_base_comfort()
        self.routes_page.set_phone()
        self.routes_page.the_next_button()
        self.routes_page.code_number()
        self.routes_page.send_cell_info()
        assert self.routes_page.get_phone() == data.phone_number

    def test_04_add_credit_card(self):
        self.set_up_base_comfort()
        self.routes_page.click_card()
        self.routes_page.add_card()
        self.routes_page.close_window()
        assert self.routes_page.get_card_input() == data.card_number
        assert self.routes_page.get_cvv_card() == data.card_code

    def test_05_write_message_to_driver(self):
        self.set_up_base_comfort()
        self.routes_page.write_drive_message(data.message_for_driver)
        assert self.routes_page.get_message() == data.message_for_driver

    def test_06_request_blanket_and_tissues(self):
        self.set_up_base_comfort()
        self.routes_page.request_blanket_and_tissues()
        assert self.routes_page.value_blanket_and_scarves() is True

    def test_07_request_ice_cream(self):
        self.set_up_base_comfort()
        self.routes_page.request_ice_cream()
        value =self.routes_page.get_ice_cream()
        assert value == 2

    def test_08_search_taxi_modal(self):
        self.set_up_before_driver_modal()
        assert self.routes_page.get_taxi()

    def test_09_wait_for_driver_info(self):
        self.set_up_before_driver_modal()
        self.routes_page.wait_for_driver_info()
        modal_element = self.driver.find_element(*self.routes_page.modal_taxi)
        assert modal_element.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()