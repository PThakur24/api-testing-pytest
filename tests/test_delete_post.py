import requests
from utils.common_assertions import *

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert_status_code(response, 200)
    assert_response_time(response, 1)
