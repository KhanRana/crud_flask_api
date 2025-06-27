import requests
import json
import pytest
host = "http://127.0.0.1:5500"


# Test that always pass
@pytest.mark.order(1)
def test_always_passes():
    assert True


# Check the status§
@pytest.mark.order(2)
def test_status_code():
    # act
    response = requests.get(f"{host}/status")
    # assert
    assert response.status_code == 200


# Test the /create endpoint
@pytest.mark.order(3)
def test_create():
    # arrange
    data = {"name": "Wheels"}
    # act
    response = requests.post(f"{host}/create", data=data)
    # assert
    assert response.status_code == 200


# Test the /update endpoint
@pytest.mark.order(4)
def test_update():
    # arrange
    data = {"old_name": "Wheels",
            "new_name": "Alloys"}
    invalid_data = {"old_name": "no_name",
                    "new_name": "Joe"}
    # act
    response = requests.post(f"{host}/update", data=data)
    invalid_response = requests.post(f"{host}/update", data=invalid_data)
    # assert
    assert response.status_code == 200
    assert invalid_response.status_code == 404


# Test the /delete endpoint
@pytest.mark.order(5)
def test_delete():
    # arrange
    data = {"name": "Alloys"}
    invalid_data = {"name": "no_name"}
    # act
    response = requests.post(f"{host}/delete", data=data)
    invalid_response = requests.post(f"{host}/delete", data=invalid_data)

    # assert
    assert response.status_code == 200
    assert invalid_response.status_code == 404


# Get all products
@pytest.mark.order(6)
def test_list_of_products():
    # act
    response = requests.get(f"{host}")
    # assert
    assert response.status_code == 200
