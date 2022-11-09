from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LivenbergNavbar:
    LOGIN_BUTTON = (By.ID, "headlessui-menu-button-:R1d56:")
    GITHUB_LOGIN_BUTTON = (By.ID, "headlessui-menu-item-:r1:")
    GITHUB_EMAIL_INPUT = (By.ID, "login_field")
    GITHUB_PASSWORD_INPUT = (By.ID, "password")
    LIBRARY_BUTTON = (By.ID, "library")

    def __init__(self, browser):
        self.browser = browser

    def login_with_github(self):
        login_btn = self.browser.find_element(*self.LOGIN_BUTTON)
        login_btn.click()
        gh_btn = self.browser.find_element(*self.GITHUB_LOGIN_BUTTON)
        gh_btn.click()
        email_input = self.browser.find_element(*self.GITHUB_EMAIL_INPUT)
        email_input.send_keys(os.environ.get("TEST_USER"))
        password_input = self.browser.find_element(*self.GITHUB_PASSWORD_INPUT)
        password_input.send_keys(os.environ.get("TEST_PASSWORD") + Keys.RETURN)

    def enter_library(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "library"))
        ).click()
