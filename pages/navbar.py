from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.model_page import ModelPage


class LivenbergNavbar(ModelPage):
    LOGIN_BUTTON = (By.ID, "headlessui-menu-button-:R1d56:")
    GITHUB_LOGIN_BUTTON = (By.ID, "headlessui-menu-item-:r1:")
    LIBRARY_BUTTON = (By.ID, "library")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click(self.LOGIN_BUTTON)

    def click_login_with_github(self):
        self.click(self.GITHUB_LOGIN_BUTTON)

    def enter_library(self):
        self.click(
            self.wait.until(EC.visibility_of_element_located(self.LIBRARY_BUTTON))
        )
