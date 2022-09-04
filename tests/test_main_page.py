from metods import wait_element, wait_title
from selenium.webdriver.common.by import By


def test_main_page(browser):
    browser.get(url=browser.base_url)
    wait_title("Your Store", browser)
    wait_element(selector="#search", driver=browser)
    wait_element(selector="#menu", driver=browser)
    wait_element(selector=".//a[text()='Desktops']", driver=browser, by=By.XPATH)
    wait_element(selector="#carousel0", driver=browser)
