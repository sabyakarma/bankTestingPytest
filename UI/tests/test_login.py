
import pytest
from UI.pages.index import Index
from UI.pages.register import Register
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_register_user(self):
        self.index_page = Index(self.driver)
        self.index_page.click_register()
        self.register = Register(self.driver)
        self.register.enter_firstname('test1')
        self.register.enter_lastName('test1')
        self.register.enter_address('test')
        self.register.enter_cityText('test')
        self.register.enter_stateText('text')
        self.register.enter_zipCode('12345')
        self.register.enter_phoneNumber('1234567890')
        self.register.enter_ssnNumber('1235456')
        self.register.enter_userName('test')
        self.register.enter_password('test')
        self.register.enter_confirm('test')
        self.register.click_registerButton()

    def test_login(self,get_userDetails):
        self.index_page = Index(self.driver)
        self.index_page.login_paraBank(get_userDetails["username"],get_userDetails["password"])
        time.sleep(20)