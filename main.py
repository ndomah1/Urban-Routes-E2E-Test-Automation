import time
import data
import helpers

from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print(' Connected to the Urban Routes server" ------>')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running------>')

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_pages.get_from() == data.ADDRESS_FROM
        assert routes_pages.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_supportive_plan_card()
        assert routes_pages.get_active_plan_card() == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        phone = data.PHONE_NUMBER
        routes_pages.set_phone(phone)
        time.sleep(3)
        assert routes_pages.get_phone() == phone

    def test_fill_card(self):
        self.driver.maximize_window()
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_pages.get_current_payment_method() == 'Card'

    def test_comment_for_driver(self):
        self.driver.maximize_window()
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_supportive_plan_card()
        routes_pages.set_message(data.MESSAGE_FOR_DRIVER)
        assert routes_pages.get_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.maximize_window()
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_supportive_plan_card()
        routes_pages.set_handkerchiefs()
        assert routes_pages.get_handkerchiefs()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_supportive_plan_card()
        routes_pages.set_icecream_order(2)
        time.sleep(3)
        assert routes_pages.get_ice_cream_count() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_supportive_plan_card()
        routes_pages.set_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(3)
        routes_pages.click_order_taxi_button()
        time.sleep(3)
        assert routes_pages.is_order_taxi_popup()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
