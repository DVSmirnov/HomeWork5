from metods import wait_element, wait_title
from selenium.webdriver.common.by import By


def test_katalog(browser):
    browser.get(url=browser.base_url + '/desktops/test')
    wait_title("Apple Cinema 30", browser)
    wait_element(selector=".//li/h2", driver=browser, by=By.XPATH)
    wait_element(selector=".fa.fa-heart", driver=browser)
    wait_element(selector=".thumbnails", driver=browser)
    wait_element(selector="#product-product", driver=browser)
