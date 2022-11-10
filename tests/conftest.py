import pytest
import selenium.webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="headlesschrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "firefox":
        driver = selenium.webdriver.Firefox()

    elif browser == "headlessfirefox":
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        driver = selenium.webdriver.Firefox(options=opts)

    elif browser == "chrome":
        driver = selenium.webdriver.Chrome()

    elif browser == "headlesschrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("--headless")
        driver = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(
            f'Browser "{browser}" not supported. --browser options: "firefox", "chrome", "headlessfirefox" or "headlesschrome"'
        )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()
