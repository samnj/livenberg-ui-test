import pytest

from pages.home import LivenbergHomePage
from pages.result import LivenbergResultPage


@pytest.mark.parametrize("query", ["  AusteN  ", "leo   tolsToy  "])
def test_search_from_home(driver, query):
    home_page = LivenbergHomePage(driver)
    result_page = LivenbergResultPage(driver)

    # Given the home page loaded
    home_page.load()

    # When we search for an author
    home_page.search(query)

    # Then the query result is lower case, trimmed and joined by + signs
    searchedQuery = result_page.author()
    q = query.lower().split()
    expected_query = "+".join(q)
    assert searchedQuery == expected_query

    # And the URL query string is lower case and joined by %2B
    url_query = result_page.url_query()
    q = query.lower().split()
    expected_query = "%2B".join(q)
    assert url_query == expected_query
