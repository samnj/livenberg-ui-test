from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LivenbergLibraryPage:
    URL = "https://livenberg.vercel.app/library"
    LIBRARY_BOOKS = (By.ID, "libraryBooks")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

        try:
            WebDriverWait(self.browser, 2).until(
                EC.url_to_be("https://livenberg.vercel.app/")
            )
        except:
            pass
