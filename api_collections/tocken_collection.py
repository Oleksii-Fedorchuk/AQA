from api_collections.base_api import BaseAPI
from api_collections.config_file import USERNAME, PASSWORD


class TokenCollection(BaseAPI):
    def __init__(self):
        super().__init__()
        self._booking_url = "booking"
        self._token_url = "auth"

    def get_token(self):
        response = self.post(f"{self._token_url}", body={"username": USERNAME, "password": PASSWORD})
        return response
