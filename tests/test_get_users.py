import requests
from utils.common_assertions import *

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    json_data = response.json()

    assert_status_code(response, 200)
    assert_response_time(response, 1)
    assert isinstance(json_data, list), "Expected a list of users"

    expected_keys = ["id", "name", "username", "email"]
    assert_keys_in_response(json_data[0], expected_keys)
