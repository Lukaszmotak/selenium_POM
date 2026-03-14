from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By

class Locators:
    FIRST_NAME = (By.ID, "customer_firstname")

class CreateAccountPage(BasePage):
    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)


    def _verify_page(self):
        # TODO: Improve this code
        sleep(3)
