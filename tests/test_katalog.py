from metods import wait_element, wait_title


def test_katalog(browser):
    browser.get(url=browser.base_url + '/desktops')
    wait_title("Desktops", browser)
    wait_element(selector="#product-category", driver=browser)
    wait_element(selector="#content", driver=browser)
    wait_element(selector="#compare-total", driver=browser)
    wait_element(selector="#grid-view", driver=browser)
