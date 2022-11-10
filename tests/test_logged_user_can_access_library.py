from pages.navbar import LivenbergNavbar
from pages.home import LivenbergHomePage
from pages.library import LivenbergLibraryPage
from pages.github_login_page import GithubLoginPage


def test_logged_user_can_access_library(driver):
    navbar = LivenbergNavbar(driver)
    home_page = LivenbergHomePage(driver)
    library_page = LivenbergLibraryPage(driver)
    github_login_page = GithubLoginPage(driver)

    # Given the home page loaded
    home_page.load()

    # When a user logs in using github
    navbar.click_login_btn()
    navbar.click_login_with_github()
    github_login_page.login()

    # Then it can access the Library clicking the 'My Books' button
    navbar.enter_library()
    assert "Total books in library:" in library_page.get_user_books_count()
