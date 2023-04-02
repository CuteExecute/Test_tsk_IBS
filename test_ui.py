import json
from time import sleep
import re
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import data
import utils

URL = "https://reqres.in"

criterion_time_delta = timedelta(
    hours=1
)


def clear_html_tags(content):
    return re.sub(r'\<[^>]*\>', '', content)


# pytest test_ui.py::test_get_resource_list_ui -s -v
def test_get_resource_list_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' List <resource> ']")
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
    expected = data.data_get_resource_list()
    assert json_response == expected


# pytest test_ui.py::test_get_users_list_ui -s -v
def test_get_users_list_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' List users ']")
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
    expected = data.data_get_users_list_page2()
    assert json_response == expected


# pytest test_ui.py::test_get_resource_ui -s -v
def test_get_resource_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Single <resource> ']")
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
    expected = data.data_get_resource()
    assert json_response == expected


# pytest test_ui.py::test_get_resource_negative_ui -s -v
def test_get_resource_negative_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[contains(text(), 'Single <resource> not found')]")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "404"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = {}
    assert json_response == expected


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


# pytest test_ui.py::test_get_user_negative_ui -s -v
def test_get_user_negative_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[contains(text(), ' Single user not found ')]")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "404"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = {}
    assert json_response == expected


# pytest test_ui.py::test_post_user_create_ui -s -v
def test_post_user_create_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Create ']")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "201"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = data.data_post_user_create()

    assert json_response["name"] == expected["name"]
    assert json_response["job"] == expected["job"]

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["createdAt"], json_response["createdAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_ui.py::test_put_user_update_ui -s -v
def test_put_user_update_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//li[@data-id='put']/*[text()=' Update ']")
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
    expected = data.data_user_update()

    assert json_response["name"] == expected["name"]
    assert json_response["job"] == expected["job"]

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["updatedAt"], json_response["updatedAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_ui.py::test_patch_user_update_ui -s -v
def test_patch_user_update_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//li[@data-id='patch']/*[text()=' Update ']")
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
    expected = data.data_user_update()

    assert json_response["name"] == expected["name"]
    assert json_response["job"] == expected["job"]

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["updatedAt"], json_response["updatedAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_ui.py::test_delete_user_ui -s -v
def test_delete_user_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[contains(text(), ' Delete ')]")
    request_button.click()
    sleep(2)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "204"


# pytest test_ui.py::test_post_register_ui -s -v
def test_post_register_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Register - successful ']")
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
    expected = data.data_post_register()
    assert json_response == expected


# pytest test_ui.py::test_post_register_negative_ui -s -v
def test_post_register_negative_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Register - unsuccessful ']")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "400"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = data.data_error_missing_pass()
    assert json_response == expected


# pytest test_ui.py::test_post_login_ui -s -v
def test_post_login_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Login - successful ']")
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
    expected = data.data_post_login()
    assert json_response == expected


# pytest test_ui.py::test_post_login_negative_ui -s -v
def test_post_login_negative_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Login - unsuccessful ']")
    request_button.click()
    sleep(1)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "400"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = data.data_error_missing_pass()
    assert json_response == expected


# pytest test_ui.py::test_get_users_delayed_ui -s -v
def test_get_users_delayed_ui(get_driver):
    # get driver
    driver = get_driver
    driver.get(URL)

    # click request
    request_button = driver.find_element(By.XPATH, r"//*[text()=' Delayed response ']")
    request_button.click()
    sleep(5)

    # get and check status code
    status_code = driver.find_element(By.XPATH, r"//*[text()='Response ']/span")
    assert status_code.text == "200"

    # get and check json response
    response = driver.find_element(By.XPATH, r"//pre[contains(@data-key, 'output-response')]") \
        .get_attribute('innerHTML')
    clear_response = clear_html_tags(response)
    json_response = json.loads(clear_response)

    # assertion
    expected = data.data_get_users_delayed()
    assert json_response == expected
