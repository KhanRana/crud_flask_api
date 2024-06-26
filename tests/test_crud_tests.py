import requests
import json

host = "http://127.0.0.1:5500"

# Test that always pass
def test_always_passes():
    assert True

# Check the status
def test_status_code():
    # act
    response = requests.get(f"{host}/status")
    # assert
    assert response.status_code == 200

# Get all products
def test_list_of_products():
    # act
    response = requests.get(f"{host}")
    # assert
    assert response.status_code == 200


# Test the /create endpoint
def test_create():
    # arrange
    data = {"name": "Evaline"}
    # act
    response = requests.post(f"{host}/create", data=data)
    # assert
    assert response.status_code == 200


# Test the /update endpoint
def test_update():
    # arrange
    data = {"old_name": "Evaline",
            "new_name": "Test Updated"}
    # act
    response = requests.post(f"{host}/update", data=data)

    # assert
    assert response.status_code == 200


# Test the /delete endpoint
def test_delete():
    # arrange
    data = {"name": "Test Updated"}
    # act
    response = requests.post(f"{host}/delete", data=data)
    # assert
    assert response.status_code == 200
