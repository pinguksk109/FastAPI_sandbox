import unittest
from unittest.mock import patch, MagicMock
from app.infrastructure.repository.dynamodb_repository import DynamodbRepository
from datetime import datetime, timezone

class TestDynamodbRepository(unittest.TestCase):

    @patch('dynamodb_repository.boto3.resource')
    def setUp(self, mock_boto_resource):
        self.mock_table = MagicMock()
        mock_dynamodb = MagicMock()
        mock_dynamodb.Table.return_value = self.mock_table
        mock_boto_resource.return_value = mock_dynamodb

        self.repository = DynamodbRepository()

    @patch('dynamodb_repository.datetime')
    def test_create_item(self, mock_datetime):
        id = 'test-id'
        userId = 'test-userId'

        mock_datetime.now.return_value = datetime(2023, 7, 30, tzinfo=timezone.utc)
        mock_datetime.now.return_value.isoformat.return_value = '2023-07-30T00:00:00+00:00'

        self.repository.create(id, userId)

        self.mock_table.put_item.assert_called_once_with(
            Item={
                "id": id,
                "userId": userId,
                "created_at": '2023-07-30T00:00:00+00:00'
            }
        )

if __name__ == '__main__':
    unittest.main()