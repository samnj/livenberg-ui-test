from selenium.webdriver.common.by import By
import os

from pages.model_page import ModelPage


class GithubLoginPage(ModelPage):
    GITHUB_EMAIL_INPUT = (By.ID, "login_field")
    GITHUB_PASSWORD_INPUT = (By.ID, "password")
    GITHUB_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='commit']")

    TEST_USER = os.environ.get("TEST_USER")
    TEST_PASSWORD = os.environ.get("TEST_PASSWORD")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.write_text(self.GITHUB_EMAIL_INPUT, self.TEST_USER)
        self.write_text(self.GITHUB_PASSWORD_INPUT, self.TEST_PASSWORD)
        self.click(self.GITHUB_SUBMIT_BUTTON)
