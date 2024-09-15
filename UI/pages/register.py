from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage

class Register(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    # xpath of register element

    firstNameText = (By.XPATH,"//input[@name='customer.firstName']")
    lastNameText = (By.XPATH,"//input[@name='customer.lastName']")
    addressText = (By.XPATH,"//input[@name='customer.address.street']")
    cityText = (By.XPATH,"//input[@name='customer.address.city']")
    StateText = (By.XPATH,"//input[@name='customer.address.state']")
    zipCode  = (By.XPATH,"//input[@name='customer.address.zipCode']")
    phoneNumber = (By.XPATH,"//input[@name='customer.phoneNumber']")
    ssnNumber = (By.XPATH,"//input[@name='customer.ssn']")
    usernameText = (By.XPATH,"//input[@name='customer.username']")
    passwordText = (By.XPATH,"//input[@name='customer.password']")
    confirmText = (By.XPATH,"//input[@name='repeatedPassword']")
    registerButton = (By.XPATH,"(//input[@type='submit'])[2]")

    def enter_firstname(self,name):
        self.enter_text(self.firstNameText,name)

    def enter_lastName(self,lastname):
        self.enter_text(self.lastNameText,lastname)

    def enter_address(self,address):
        self.enter_text(self.addressText,address)

    def enter_cityText(self,city):
        self.enter_text(self.cityText,city)

    def enter_stateText(self, state):
        self.enter_text(self.cityText, state)

    def enter_zipCode(self,zipcode):
        self.enter_text(self.zipCode,zipcode)

    def enter_phoneNumber(self,number:int):
        self.enter_text(self.phoneNumber,number)

    def enter_ssnNumber(self,ssn):
        self.enter_text(self.ssnNumber,ssn)

    def enter_userName(self,username):
        self.enter_text(self.usernameText,username)

    def enter_password(self,password):
        self.enter_text(self.passwordText,password)

    def enter_confirm(self,confirm):
        self.enter_text(self.confirmText,confirm)

    def click_registerButton(self):
        self.click_on_element(self.registerButton)






