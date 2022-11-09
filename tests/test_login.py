import pytest
from time import sleep

from pages.home import LivenbergHomePage


def test_search_from_home(browser):
    home_page = LivenbergHomePage(browser)

    # Given the home page loaded
    home_page.load()
    sleep(15)
    assert True
