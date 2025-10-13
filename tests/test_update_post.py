import requests
from utils.common_assertions import *

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_update_post():
    updated_data = {
        "id": 1,
        "title": "Updated Post Title",
        "body": "Updated content",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)
    json_data = response.json()

    assert_status_code(response, 200)
    assert_response_time(response, 1)
    assert_keys_in_response(json_data, ["id", "title", "body", "userId"])
    assert json_data["title"] == "Updated Post Title"
