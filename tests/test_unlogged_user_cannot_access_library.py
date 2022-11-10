from pages.library import LivenbergLibraryPage
from pages.home import LivenbergHomePage

from selenium.common.exceptions import TimeoutException


def test_unlogged_user_cannot_access_library(driver):
    library_page = LivenbergLibraryPage(driver)
    home_page = LivenbergHomePage(driver)

    # Given that the home page loaded
    home_page.load()

    # When an unlogged user tries to access the library via URL
    library_page.load()

    # Then it cannot see the library
    try:
        library_page.get_user_books_count()
    except TimeoutException:
        assert True

    # And it gets redirected to the home page
    assert (
        home_page.get_home_header() == "A Project Gutenberg search engine and library"
    )
