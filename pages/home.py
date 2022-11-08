from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LivenbergHomePage:
    URL = "https://livenberg.vercel.app/"

    SEARCH_INPUT = (By.ID, "searchBar")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, query):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query + Keys.RETURN)
