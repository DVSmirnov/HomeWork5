from metods import wait_element, wait_title


def test_admin_page(browser):
    browser.get(url=browser.base_url + '/admin/')
    wait_title("Administration", browser)
    wait_element(selector=".panel-body", driver=browser)
    wait_element(selector="#input-username", driver=browser)
    wait_element(selector="#input-password", driver=browser)
    wait_element(selector="button[type='submit']", driver=browser)
