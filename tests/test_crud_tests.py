import requests
import json

# Test that always pass
def test_always_passes ():
    assert True
    print ("Good, it always passes")

# Test that always fail
def test_always_fails ():
    assert False
    print ("Good, it always fails")

# Test the /status endpoint
def test_status ():
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200
    print ("Good, the /status endpoint is working")


def test_list_of_products ():
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
    print ("Good, the host/ endpoint is working")

# Test the /create endpoint
def test_create ():
    # act 
    data = {"name": "Evaline"}
    # arrange
    response = requests.post("http://127.0.0.1:5000/create", data=data)
    # assert
    assert response.status_code == 200
    print ("Good, the /create endpoint is working")

# Test the /update endpoint
def test_update ():
    # act
    data = {"old_name": "Evaline",
            "new_name": "Test Updated"}
    # arrange
    response = requests.post("http://127.0.0.1:5000/update", data=data)

    # assert
    assert response.status_code == 200
    print ("Good, the /update endpoint is working")

# Test the /delete endpoint
def test_delete ():
    # act
    data = {"name": "Test Updated"}
    # arrange
    response = requests.post("http://127.0.0.1:5000/delete", data=data)
    # assert
    assert response.status_code == 200
    print ("Good, the /delete endpoint is working")