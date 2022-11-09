import pytest

from pages.result import LivenbergResultPage


@pytest.mark.parametrize("URLQuery", ["austen%2Bjane", "ausTEn%2BJane"])
def test_search_from_url(browser, URLQuery):
    result_page = LivenbergResultPage(browser)

    # Given the result page loaded from a given URL query
    result_page.load(URLQuery)

    # Then the query result is lower case and joined by + signs
    searchedQuery = result_page.author()
    expected_URLQuery = URLQuery.lower().replace("%2b", "+")
    assert searchedQuery == expected_URLQuery
