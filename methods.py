from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(ES.title_is((title)))
    except TimeoutException:
        raise AssertionError("Ожидание другого наименования заголовка страницы".format(title, driver.title))


def wait_element(selector, driver, timeout=1, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(ES.visibility_of_element_located((by, selector)))
    except TimeoutException:
        driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError("Долгое ожидание элемента {}".format(selector))
