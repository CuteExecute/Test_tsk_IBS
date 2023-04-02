import requests

DOMAIN = 'https://reqres.in'


def get_users_list(page: int = 1, per_page: int = 6):
    url = f"{DOMAIN}/api/users?page={page}&per_page={per_page}"
    response = requests.get(url)
    return response


def get_user(user_id: int = 2):
    url = f"{DOMAIN}/api/users/{user_id}"
    response = requests.get(url)
    return response


def get_resource_list(resource: str = "unknown", page: int = 1, per_page: int = 6):
    url = f"{DOMAIN}/api/{resource}?page={page}&per_page={per_page}"
    response = requests.get(url)
    return response


def get_resource(resource: str = "unknown", resource_id: int = 2):
    url = f"{DOMAIN}/api/{resource}/{resource_id}"
    response = requests.get(url)
    return response


def post_user_create(json_payload):
    url = f"{DOMAIN}/api/users"
    response = requests.post(url, json=json_payload)
    return response


def put_user_update(json_payload, user_id: int = 2):
    url = f"{DOMAIN}/api/users/{user_id}"
    response = requests.put(url, json=json_payload)
    return response


def patch_user_update(json_payload, user_id: int = 2):
    url = f"{DOMAIN}/api/users/{user_id}"
    response = requests.patch(url, json=json_payload)
    return response


def delete_user(user_id: int = 2):
    url = f"{DOMAIN}/api/users/{user_id}"
    response = requests.delete(url)
    return response


def post_register(json_payload):
    url = f"{DOMAIN}/api/register"
    response = requests.post(url, json=json_payload)
    return response


def post_login(json_payload):
    url = f"{DOMAIN}/api/login"
    response = requests.post(url, json=json_payload)
    return response


def get_users_delayed(delay: int = 3):
    url = f"{DOMAIN}/api/users?delay={delay}"
    response = requests.get(url)
    return response
