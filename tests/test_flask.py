import pytest 
from flask import Flask


@pytest.mark.Success
def test_hello(client: Flask):
    response = client.test_client().get("/")
    assert b"Hello, World" in response.data




def hello():
    return "<p>Hello, James!</p>"

@pytest.mark.Mock
def test_mocked_api(mocker):
    mocker.patch('test_flask.test_hello', hello )
    assert "Hello, James" in test_hello()

@pytest.mark.pageFound
@pytest.mark.parametrize("page", [2, 4, 7])
def test_content_other_page(client, page: int):
    page = str(page)
    response = client.test_client().get("/other?page=" + page)
    assert response.status_code == 200


@pytest.mark.pageFound
@pytest.mark.parametrize("route", ["/","/other"])
def test_page_exists(client: Flask, route):
    response = client.test_client().get(str(route))
    assert response.status_code == 200


@pytest.mark.pageNotFound
@pytest.mark.parametrize("route", ["/james","/other2"])
def test_page_not_exists(client: Flask, route):
    response = client.test_client().get(str(route))
    assert response.status_code == 404


@pytest.mark.pageBiggerThan500
@pytest.mark.parametrize("page", [501, 600, 982])
def test_page_number_bigger(client, page: int):
    arg = str(page)
    response = client.test_client().get("/other?page=" + arg)
    assert response.status_code == 200
    assert  page >= 500

@pytest.mark.pageBiggerThan500Error
@pytest.mark.parametrize("page", [333, 233])
def test_page_number_bigger(client, page: int):
    with pytest.raises(ValueError):
        if page < 500:
            raise ValueError("value must be biggerthan 500")

