import pytest

def assert_status_code(response, expected_code=200):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

def assert_response_time(response, max_time=1):
    assert response.elapsed.total_seconds() < max_time, f"Response took too long: {response.elapsed.total_seconds()}s"

def assert_keys_in_response(json_data, expected_keys):
    for key in expected_keys:
        assert key in json_data, f"Missing key: {key}"
