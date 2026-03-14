from pages.base_page import BasePage

class locators:

    SIGN_IN_LINK = (By.CLASS_NAME, "login")



class HomePage(BasePage):
    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()

        pass