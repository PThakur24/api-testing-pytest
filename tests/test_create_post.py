import requests
from utils.common_assertions import *

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {
        "title": "API Automation Test",
        "body": "Testing POST request",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    json_data = response.json()

    assert_status_code(response, 201)
    assert_response_time(response, 1)
    assert_keys_in_response(json_data, ["id", "title", "body", "userId"])
    assert json_data["title"] == payload["title"]
