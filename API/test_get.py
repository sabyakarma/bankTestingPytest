import pytest
import requests
import json

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
post_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


def test_getProductList():
    response = requests.get(url=BASE_URL)

    response_json = response.json()
    assert response.status_code == 200, f"No Response, Status code:{response.status_code}"
    # json_path = r"API/responseData/ProductList.json"
    # with open("productList.json", "w") as json_file:
    #     json.dump(response_json, json_file, indent=4)


def test_postProduct():
    dump = {
        "id": 1,
        "title": "test title",
        "dueDate": "2024-09-15T07:42:13.148Z",
        "completed": True
    }
    response = requests.post(url=post_url, json=dump)

    assert response.status_code == 201 or response.status_code == 200, f"Post Failed Code:{response.status_code}"


def test_updateProduct():
    id = 2
    put_url = f"https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}"

    dump = {
        "id": 1,
        "title": "test title",
        "dueDate": "2024-09-15T07:42:13.148Z",
        "completed": True
    }

    response = requests.put(url=put_url, json=dump)

    assert response.status_code == 200, f"Put Failed, {response.status_code}"


def test_deleteProduct():
    id = 1
    delete_url = f"https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}"

    response = requests.delete(url=delete_url)
    assert response.status_code == 200, f"Delete Failed, {response.status_code}"
