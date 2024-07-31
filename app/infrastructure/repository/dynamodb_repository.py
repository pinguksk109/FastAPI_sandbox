import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from datetime import datetime, timezone

class DynamoDBRepository:
    def __init__(self):
        self.dyn_resource = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='local',
        aws_secret_access_key='local', endpoint_url='http://localhost:8000')
        self.table = self.dyn_resource.Table('ot-test')

    def create(self, id, userId):
        try:
            current_utc_time = datetime.now(timezone.utc)
            current_utc_time_iso = current_utc_time.isoformat()  # ISO 8601形式に変換
            print(current_utc_time_iso)
            self.table.put_item(
                Item={
                    "id": id,
                    "userId": userId,
                    "created_at": current_utc_time_iso
                }
            )
        except ClientError as err:
            raise
    
    def add(self, id, user_id):
        try:
            response = self.table.update_item(
                Key={
                    'id': id,
                    'userId': user_id
                },
                UpdateExpression="set #status = :status_value",
                ExpressionAttributeNames={
                    '#status': 'status'
                },
                ExpressionAttributeValues={
                    ':status_value': "OK"
                },
                ReturnValues="UPDATED_NEW"
            )
            print(response)
        except ClientError as err:
            raise
    
    def scan(self, userId):

        # 公式ドキュメントの書き方
        movies = []
        scan_kwargs = {
            "FilterExpression": Attr('userId').eq(userId) & Attr('created_at').between('2024-07-01', '2024-07-31')
            # "ProjectionExpression": "#yr, title, info.rating",
            # "ExpressionAttributeNames": {"#yr": "year"},
        }
        try:
            done = False
            start_key = None
            while not done:
                if start_key:
                    scan_kwargs["ExclusiveStartKey"] = start_key
                response = self.table.scan(**scan_kwargs)
                movies.extend(response.get("Items", []))
                start_key = response.get("LastEvaluatedKey", None)
                done = start_key is None

        except ClientError as err:
            raise
    
        return movies

    async def get_mock_data(self, organization_id: str) -> dict:
        return {"item1": "data1", "item2": "data2"}