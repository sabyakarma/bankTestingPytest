import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.mark.usefixtures("")
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # define the xpaths

    def click_on_element(self, element: tuple):
        self.driver.find_element(*element).click()

    def enter_text(self,element:tuple,text):
        self.driver.find_element(*element).send_keys(text)

    def return_text(self, text, element: tuple):
        return self.driver.find_element(*element).text
