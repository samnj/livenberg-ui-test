from selenium.webdriver.common.by import By

from pages.model_page import ModelPage


class LivenbergResultPage(ModelPage):
    SEARCH_RESULTS = (By.ID, "searchResults")
    URL = "https://livenberg.vercel.app/results/books?search="

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, URLQuery):
        self.driver.get(self.URL + URLQuery)

    def count(self):
        result = self.driver.find_element(*self.SEARCH_RESULTS)
        count = result.text.split()[0]
        return count

    def author(self):
        result = self.driver.find_element(*self.SEARCH_RESULTS)
        author = result.text.split('"')[1]
        return author

    def url_query(self):
        url = self.driver.current_url
        query = url.split("=")[1]
        return query
