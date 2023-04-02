from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://reqres.in'


# pytest test_ui.py::test_list_users_ui -s -v
def test_list_users_ui():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    driver.close()
