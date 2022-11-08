from selenium.webdriver.common.by import By


class LivenbergResultPage:
    SEARCH_RESULTS = (By.ID, "searchResults")

    def __init__(self, browser):
        self.browser = browser

    def count(self):
        result = self.browser.find_element(*self.SEARCH_RESULTS)
        count = result.text.split()[0]
        return count

    def author(self):
        result = self.browser.find_element(*self.SEARCH_RESULTS)
        author = result.text.split('"')[1]
        return author

    def url_query(self):
        url = self.browser.current_url
        query = url.split("=")[1]
        return query
