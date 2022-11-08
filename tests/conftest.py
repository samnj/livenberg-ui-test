import pytest
import selenium.webdriver
import json


@pytest.fixture
def config(scope="session"):
    with open("config.json") as config_file:
        config = json.load(config_file)

    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    return config


@pytest.fixture
def browser(config):
    if config["browser"] == "Firefox":
        browser = selenium.webdriver.Firefox()

    elif config["browser"] == "Chrome":
        browser = selenium.webdriver.Chrome()

    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        browser = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'{config["browser"]} not supported')

    browser.implicitly_wait(config["implicit_wait"])

    yield browser

    browser.quit()
