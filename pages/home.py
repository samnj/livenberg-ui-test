from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.model_page import ModelPage


class LivenbergHomePage(ModelPage):
    URL = "https://livenberg.vercel.app/"
    SEARCH_INPUT = (By.ID, "searchBar")
    HOME_HEADER = (By.CSS_SELECTOR, "h1")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        self.write_text(search_input, query)
        search_input.submit()

    def get_home_header(self):
        return self.get_text(self.HOME_HEADER)
