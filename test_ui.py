import json
from time import sleep
import re

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import data

URL = "https://reqres.in"


def clear_html_tags(content):
    return re.sub(r'\<[^>]*\>', '', content)


def test_get_resource_list_ui(get_driver):
    driver = get_driver
    pass


def test_get_users_list_ui(get_driver):
    driver = get_driver
    pass


def test_get_resource_ui(get_driver):
    driver = get_driver
    pass


def test_get_resource_negative_ui(get_driver):
    driver = get_driver
    pass


# pytest test_ui.py::test_get_user_ui -s -v
def test_get_user_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Single user ']")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "200"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = data.data_get_user()
    assert json_response == expected


def test_get_user_negative_ui(get_driver):
    driver = get_driver
    pass


def test_post_user_create_ui(get_driver):
    driver = get_driver
    pass


def test_put_user_update_ui(get_driver):
    driver = get_driver
    pass


def test_patch_user_update_ui(get_driver):
    driver = get_driver
    pass


def test_delete_user_ui(get_driver):
    driver = get_driver
    pass


def test_post_register_ui(get_driver):
    driver = get_driver
    pass


def test_post_register_negative_ui(get_driver):
    driver = get_driver
    pass


def test_post_login_ui(get_driver):
    driver = get_driver
    pass


def test_post_login_negative_ui(get_driver):
    driver = get_driver
    pass


def test_get_users_delayed_ui(get_driver):
    driver = get_driver
    pass
