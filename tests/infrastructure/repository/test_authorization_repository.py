import unittest
from unittest.mock import patch, Mock
from unittest import mock
from http import HTTPStatus

from app.domain.auth_token import AuthToken
from app.exception.api_response_exception import ApiResponseException
from app.exception.authorization_exception import AuthorizationException
from app.infrastructure.repository.authorization_repository import AuthorizationRepository

class TestAuthorizationRepository(unittest.TestCase):
    @mock.patch('requests.get')
    def test_HTTPステータスコード200の場合_戻り値がNullであること(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.OK
        mock_get.return_value = mock_response

        auth_token = AuthToken("xxxxx")
        repository = AuthorizationRepository(auth_token)

        actual = repository.send_request()
        self.assertIsNone(actual)

    @mock.patch('requests.get')
    def test_HTTPステータスコード401の場合_AuthorizationExceptionをスローすること(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.UNAUTHORIZED
        mock_get.return_value = mock_response

        auth_token = AuthToken("xxxxx")
        repository = AuthorizationRepository(auth_token)

        with self.assertRaises(AuthorizationException):
            repository.send_request()

    @mock.patch('requests.get')
    def test_HTTPステータスコード403の場合_AuthorizationExceptionをスローすること(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.FORBIDDEN
        mock_get.return_value = mock_response

        auth_token = AuthToken("xxxxx")
        repository = AuthorizationRepository(auth_token)

        with self.assertRaises(AuthorizationException):
            repository.send_request()

    @mock.patch('requests.get')
    def test_HTTPステータスコード500の場合_ApiResponseExceptionをスローすること(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        mock_get.return_value = mock_response

        auth_token = AuthToken("xxxxx")
        repository = AuthorizationRepository(auth_token)

        with self.assertRaises(ApiResponseException):
            repository.send_request()

if __name__ == '__main__':
    unittest.main()