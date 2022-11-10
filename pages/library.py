from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.model_page import ModelPage


class LivenbergLibraryPage(ModelPage):
    URL = "https://livenberg.vercel.app/library"
    LIBRARY_BOOKS = (By.ID, "libraryBooks")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get(self.URL)

    def get_user_books_count(self):
        return self.get_text(self.LIBRARY_BOOKS)
