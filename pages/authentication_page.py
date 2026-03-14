from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage


class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")


class AuthenticationPage(BasePage):

    def enter_create_account_email(self, email):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)
        pass

    def click_create_account(self):

        self.driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
        return CreateAccountPage(self.driver)