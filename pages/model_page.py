from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class ModelPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, element):
        el = self.wait.until(EC.element_to_be_clickable(element))
        el.click()

    def write_text(self, element, text):
        el = self.wait.until(EC.element_to_be_clickable(element))
        el.send_keys(text)

    def get_text(self, element):
        el = self.wait.until(EC.visibility_of_element_located(element))
        return el.text

    def is_displayed(self, element):
        try:
            element.is_displayed()
        except NoSuchElementException:
            return False
