import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser for tests"
    )

    parser.addoption(
        "--drivers", default=os.path.expanduser("C:/Drivers"), help="drivers for browsers"
    )

    parser.addoption(
        "--headless", default="store_true", help="default page"
    )

    parser.addoption(
        "--base_url", default="http://192.168.0.105:8081/", help="default ip"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers_folder = request.config.getoption("--drivers")
    base_url = request.config.getoption("--base_url")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.headless = True

        driver = webdriver.Chrome(
            executable_path=os.path.expanduser(f"{drivers_folder}/chromedriver"),
            options=options
        )
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=os.path.expanduser(f"{drivers_folder}/geckodriver")
        )
    elif browser_name == "edge":
        driver = webdriver.Edge(
            executable_path=os.path.expanduser(f"{drivers_folder}/msedgedriver")
        )
    else:
        raise ValueError(f"Browser {browser_name} ne rabotaet")
    driver.base_url = base_url
    yield driver

    driver.close()
