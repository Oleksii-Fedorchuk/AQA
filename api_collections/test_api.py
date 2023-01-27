# from requests import get
# from http import HTTPStatus
#
# from api_collections.config_file import BASE_URL
# from api_collections.booking_collection import BookingCollection
# from api_collections.tocken_collection import TokenCollection
#
#
# def test_get_status_200():
#     response = get(f"{BASE_URL}")
#     assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
#                                                   f"Expected: {HTTPStatus.OK}"
#
#
# def test_create_booking():
#     response = BookingCollection().create_booking()
#     assert response.status_code == HTTPStatus.OK
#
#
# def test_get_booking_id():
#     response = BookingCollection().get_booking_id()
#     assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
#                                                   f"Expected: {HTTPStatus.OK}"
#
#
# def test_getting_token():
#     response = TokenCollection().get_token()
#     assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
#                                                   f"Expected: {HTTPStatus.OK}"
