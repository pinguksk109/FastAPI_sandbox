import unittest
from unittest.mock import patch, MagicMock
from app.infrastructure.repository.s3_repository import S3Repository

class TestS3Repository(unittest.TestCase):

    @patch('boto3.client')
    def test_アップロードに成功した場合_uploadが1度呼び出されていること(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        repository = S3Repository('http://localhost:9000')
        actual = repository.put('test.txt', 'test-bucket')

        self.assertIsNone(actual)
        mock_s3_client.upload_file.assert_called_once_with('test.txt', 'test-bucket', 'test.txt')

if __name__ == '__main__':
    unittest.main()
