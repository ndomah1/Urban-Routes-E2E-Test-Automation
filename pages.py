import time
import helpers

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')

    phone_number = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Phone number")]')
    phone_number_input = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, "phone")
    phone_next_button = (By.XPATH, "//button[text()='Next']")
    phone_number_code_input = (By.ID, 'code')
    phone_confirm_button = (By.XPATH, "//button[text()='Confirm']")

    payment_method = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')
    add_card_button = (By.XPATH, '//div[contains(text(),"Add card")]')
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    link_button = (By.XPATH, "//button[text()='Link']")
    # card_title = (By.XPATH, '//div[text()= "Adding a card"]')
    close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')

    message_to_driver = (By.ID, 'comment')

    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')

    icecream_add_option = (By.CLASS_NAME, 'counter-plus')
    icecream_amount_option = (By.CLASS_NAME, 'counter-value')

    order_car_button = (By.CLASS_NAME, 'smart-button-wrapper')
    order_popup = (By.CLASS_NAME, 'order-body')

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Address
    def set_from(self, from_address):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Call a Taxi
    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    # Supportive plan
    def click_supportive_plan_card(self):
        self.driver.find_element(*self.supportive_plan_card).click()

    def get_active_plan_card(self):
        return self.driver.find_element(*self.active_plan_card).text

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    # Phone number
    def get_phone(self):
        return self.driver.find_element(*self.phone_number_input).text

    def set_phone(self, phone):
        self.driver.find_element(*self.phone_number).click()
        time.sleep(3)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        time.sleep(3)
        self.driver.find_element(*self.phone_next_button).click()
        time.sleep(3)
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code_input).send_keys(code)
        self.driver.find_element(*self.phone_confirm_button).click()

    # Payment methods
    def set_card(self, card_number, card_code):
        self.driver.find_element(*self.payment_method).click()
        time.sleep(3)
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_input).send_keys(card_number)
        self.driver.find_element(*self.card_code_input).send_keys(card_code)
        self.driver.find_element(*self.link_button).click()
        time.sleep(3)
        self.driver.find_element(*self.close_button).click()
        time.sleep(3)

    def get_current_payment_method(self):
        return self.driver.find_element(*self.current_payment_method).text

    # Comment for the Driver
    def set_message(self, message):
        self.driver.find_element(*self.message_to_driver).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_to_driver).get_property('value')

    # Ordering a Blanket and Handkerchiefs
    def set_handkerchiefs(self):
        switches = self.driver.find_elements(*self.option_switches)
        switches[0].click()
        self.get_handkerchiefs()

    def get_handkerchiefs(self):
        switches = self.driver.find_elements(*self.option_switches_inputs)
        return switches[0].get_property('checked')

    # Ordering 2 Ice Creams
    def get_ice_cream_count(self):
        return self.driver.find_element(*self.icecream_amount_option).text

    def set_icecream_order(self, number_of_icecream):
        option_add_controls = self.driver.find_elements(*self.icecream_add_option)
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        for count in range(number_of_icecream):
            option_add_controls[0].click()

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_car_button).click()

    def is_order_taxi_popup(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_popup))
        return self.driver.find_element(*self.order_popup).is_displayed()
