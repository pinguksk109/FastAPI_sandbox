import boto3
from botocore.exceptions import NoCredentialsError

class S3Repository:
    def __init__(self, endpoint_url, region_name):
        self.s3_client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            region_name=region_name
        )

    def put(self, object_name, bucket_name, key):

        try:
            self.s3_client.upload_file(object_name, bucket_name, key)
            return
        except FileNotFoundError:
            return False
        except NoCredentialsError:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

# TODO: 消す
if __name__ == "__main__":
    endpoint_url = 'http://localhost:9000'
    aws_secret_access_key = 'your-secret-key'
    region_name='us-west-1'

    s3_repository = S3Repository(endpoint_url, region_name)
    
    key = 'path/'
    object_name = 'text.txt'
    bucket_name = 'test'
    
    key = 'path/'
    object_name = 'text.txt'
    bucket_name = 'test'
    
    s3_repository.put(object_name, bucket_name, key)