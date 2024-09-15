from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage



class Index(BasePage):

    def __init__(self,driver):

        super().__init__(driver)


    # Customer Login
    username = (By.XPATH,"//input[@name = 'username']")
    password = (By.XPATH,"//input[@name = 'password']")
    submit = (By.XPATH,"//input[@type = 'submit']")
    register = (By.XPATH,"//a[text() = 'Register']")


    def login_paraBank(self,username,password):
        self.enter_text(self.username,text=username)
        self.enter_text(self.password,text=password)
        self.click_on_element(self.submit)

    def click_register(self):
        self.click_on_element(self.register)

