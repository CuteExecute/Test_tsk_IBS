import pytest
from datetime import datetime, timedelta
import endpoints
import data
import utils

criterion_time_delta = timedelta(
    hours=1
)


# pytest test_main.py::test_get_resource_list -s -v
def test_get_resource_list():
    expected = data.data_get_resource_list()

    response = endpoints.get_resource_list()
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_get_users_list -s -v
def test_get_users_list():
    expected = data.data_get_users_list()

    response = endpoints.get_users_list()
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_get_resource -s -v
def test_get_resource():
    expected = data.data_get_resource()

    response = endpoints.get_resource()
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_get_resource_negative -s -v
def test_get_resource_negative():
    expected = {}

    response = endpoints.get_resource("unknown", 23)
    assert response.status_code == 404
    assert response.json() == expected


# pytest test_main.py::test_get_user -s -v
def test_get_user():
    expected = data.data_get_user()

    response = endpoints.get_user()
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_get_user_negative -s -v
def test_get_user_negative():
    expected = {}

    response = endpoints.get_user(23)
    assert response.status_code == 404
    assert response.json() == expected


# pytest test_main.py::test_post_user_create -s -v
def test_post_user_create():
    expected = data.data_post_user_create()
    params = {
        "name": "morpheus",
        "job": "leader"
    }

    response = endpoints.post_user_create(params)
    assert response.status_code == 201
    assert response.json()["name"] == expected["name"]
    assert response.json()["job"] == expected["job"]
    assert isinstance(response.json()["id"], str)

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["createdAt"], response.json()["createdAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_main.py::test_put_user_update -s -v
def test_put_user_update():
    expected = data.data_user_update()
    params = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = endpoints.put_user_update(params)
    assert response.status_code == 200
    assert response.json()["name"] == expected["name"]
    assert response.json()["job"] == expected["job"]

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["updatedAt"], response.json()["updatedAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_main.py::test_patch_user_update -s -v
def test_patch_user_update():
    expected = data.data_user_update()
    params = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = endpoints.patch_user_update(params)
    assert response.status_code == 200
    assert response.json()["name"] == expected["name"]
    assert response.json()["job"] == expected["job"]

    # Checking the difference in time at one hour
    difference_in_time = utils.difference_time(expected["updatedAt"], response.json()["updatedAt"])
    assert difference_in_time < criterion_time_delta


# pytest test_main.py::test_delete_user -s -v
def test_delete_user():
    user_id = 2

    response = endpoints.delete_user(user_id)
    assert response.status_code == 204


# pytest test_main.py::test_post_register -s -v
def test_post_register():
    expected = data.data_post_register()
    params = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = endpoints.post_register(params)
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_post_register_negative -s -v
def test_post_register_negative():
    expected = data.data_error_missing_pass()
    params = {
        "email": "sydney@fife"
    }

    response = endpoints.post_register(params)
    assert response.status_code == 400
    assert response.json() == expected


# pytest test_main.py::test_post_login -s -v
def test_post_login():
    expected = data.data_post_login()
    params = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = endpoints.post_login(params)
    assert response.status_code == 200
    assert response.json() == expected


# pytest test_main.py::test_post_login_negative -s -v
def test_post_login_negative():
    expected = data.data_error_missing_pass()
    params = {
        "email": "peter@klaven"
    }

    response = endpoints.post_login(params)
    assert response.status_code == 400
    assert response.json() == expected


# pytest test_main.py::test_get_users_delayed -s -v
def test_get_users_delayed():
    delay = 1
    expected = data.data_get_users_delayed()

    response = endpoints.get_users_delayed(delay)
    assert response.status_code == 200
    assert response.json() == expected
