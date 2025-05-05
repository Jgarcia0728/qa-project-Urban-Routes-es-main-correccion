import data
import localizadores
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver


    def set_from(self, from_address):
        #self.driver.find_element(*localizadores.UrbanRoutesPage.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*localizadores.UrbanRoutesPage.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
           EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.to_field).get_property('value')

    def click_order_a_taxi_button(self):
        wait = WebDriverWait(self.driver, 5)
        order_taxi_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.round")))
        order_taxi_button.click()

    def click_fare_comfort(self):
        wait = WebDriverWait(self.driver, 5)
        fare_comfort = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')))
        fare_comfort.click()

    def select_button_number(self):
        wait = WebDriverWait(self.driver, 5)
        button_number = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"np-text")))
        button_number.click()

    def phone_number(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.phone_number_field).send_keys(data.phone_number)

    def set_phone(self):
        self.select_button_number()
        self.phone_number()

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 5)
        p_next_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()=\"Siguiente\"]")))
        p_next_button.click()

    def send_cell_info(self):
        wait = WebDriverWait(self.driver, 5)
        conf_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Confirmar"]')))
        conf_button.click()

    def get_phone(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.phone_number_field).get_property('value')

    def code_phone_click(self):
        wait = WebDriverWait(self.driver, 5)
        code_phone = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='code']")))
        code_phone.click()

    def code_number(self):
        phone_code = helpers.retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*localizadores.UrbanRoutesPage.code_phone_button).send_keys(phone_code)

    def get_code(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.code_phone_button).get_property('value')

    def method_pay_click(self):
        wait = WebDriverWait(self.driver, 5)
        method_pay = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp-button.filled")))
        method_pay.click()

    def add_card_click(self):
        wait = WebDriverWait(self.driver, 5)
        add_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp-row.disabled")))
        add_card.click()

    def click_card(self):
        self.method_pay_click()
        self.add_card_click()

    def number_card_click(self):
        wait = WebDriverWait(self.driver, 5)
        credit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-number-input')))
        credit.click()

    def number_input(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.card_numbers).send_keys(data.card_number)

    def card_input(self):
        self.number_card_click()
        self.number_input()

    def get_card_input(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.card_numbers).get_property('value')

    def cvv_add(self):
        wait = WebDriverWait(self.driver, 5)
        cvv = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')))
        cvv.click()

    def code_card_input(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.card_cvv).send_keys(data.card_code)

    def cvv_code(self):
        self.code_card_input()

    def get_cvv_card(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.card_cvv).get_property('value')

    def registered_card(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.add_card_button).click()

    def add_card(self):
        self.card_input()
        self.cvv_code()
        self.registered_card()

    def close_window(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.close_button).click()

    def write_drive_message(self, message):
        message_field = self.driver.find_element(*localizadores.UrbanRoutesPage.message_driver)
        message_field.send_keys(data.message_for_driver)

    def get_message(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.message_driver).get_property('value')

    def request_blanket_and_scarves(self):
        wait = WebDriverWait(self.driver, 5)
        blanket_scarves = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')))
        blanket_scarves.click()

    def get_blanket_and_scarves(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.add_blankets_scarves).get_property('value')

    def request_ice_cream(self):
        wait = WebDriverWait(self.driver, 5)
        o_icecream = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "counter-plus")))
        o_icecream.click()
        o_icecream.click()


    def get_ice_cream(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.order_icecream).get_property('value')


    def order_taxi(self):
        wait = WebDriverWait(self.driver, 5)
        o_taxi = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "smart-button-main")))
        o_taxi.click()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
