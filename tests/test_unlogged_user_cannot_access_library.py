from pages.navbar import LivenbergNavbar
from pages.library import LivenbergLibraryPage
from pages.home import LivenbergHomePage


def test_unlogged_user_cannot_access_library(browser):
    library_page = LivenbergLibraryPage(browser)
    home_page = LivenbergHomePage(browser)
    navbar = LivenbergNavbar(browser)

    # Given that the home page loaded
    home_page.load()

    # When an unlogged user tries to access the library via URL
    library_page.load()

    # Then it gets redirected to the home page
    assert browser.current_url == "https://livenberg.vercel.app/"
