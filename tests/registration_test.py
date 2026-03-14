from tests.base_test import BaseTest

class RegistartionTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email("test@test.pl")

    def testNoSurname(self):
        pass