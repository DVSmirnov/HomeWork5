from metods import wait_element, wait_title


def test_admin_page(browser):
    browser.get(url=browser.base_url + '/index.php?route=account/register')
    wait_title("Register Account", browser)
    wait_element(selector="#content", driver=browser)
    wait_element(selector="#column-right", driver=browser)
    wait_element(selector="input[type='submit']", driver=browser)
    wait_element(selector=".pull-right", driver=browser)
