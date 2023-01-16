from requests import get
from http import HTTPStatus

from Automation_tests.api_collections.config_file import BASE_URL
from Automation_tests.api_collections.booking_collection import BookingCollection


def test_get_status_200():
    response = get(f"{BASE_URL}")
    assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
                                                  f"Expected: {HTTPStatus.OK}"


def test_create_booking():
    response = BookingCollection().create_booking()
    c = 0
    print(response.text)
    assert response.status_code == HTTPStatus.OK


def test_get_booking_id():
    response = BookingCollection().get_booking_id()
    c = 0
    print(response.text)
    assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
                                                  f"Expected: {HTTPStatus.OK}"


def test_getting_token():
    response = BookingCollection().get_token()
    print(response.text)
    assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
                                                  f"Expected: {HTTPStatus.OK}"
