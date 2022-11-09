from pages.home import LivenbergHomePage
from pages.navbar import LivenbergNavbar
from pages.library import LivenbergLibraryPage


def test_logged_user_can_access_library(browser):
    home_page = LivenbergHomePage(browser)
    library_page = LivenbergLibraryPage(browser)

    navbar = LivenbergNavbar(browser)

    # Given the home page loaded
    home_page.load()

    # When a user logs in using github
    navbar.login_with_github()

    # Then it can access the Library clicking the 'My Books' button
    navbar.enter_library()
    assert browser.current_url == "https://livenberg.vercel.app/library"

    # And it can access the Library via URL
    home_page.load()
    library_page.load()
    assert browser.current_url == "https://livenberg.vercel.app/library"
