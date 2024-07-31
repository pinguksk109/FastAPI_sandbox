from http import HTTPStatus
import requests

from app.domain.auth_token import AuthToken
from app.exception.api_response_exception import ApiResponseException
from app.exception.authorization_exception import AuthorizationException

class AuthorizationRepository:
    def __init__(self, auth_token: AuthToken):
        self.auth_token = auth_token

    def send_request(self):
        url = "http://localhost:3000/posts"
        headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == HTTPStatus.OK:
            return
        elif response.status_code in [HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN]:
            raise AuthorizationException(response.status_code, f"Authorization error: {response.status_code}")
        else:
            raise ApiResponseException(response.status_code, f"API response error: {response.status_code}")
