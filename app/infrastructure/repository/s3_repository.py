import boto3
from botocore.exceptions import NoCredentialsError

class S3Repository:
    def __init__(self, endpoint_url):
        self.s3_client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
        )

    def put(self, file_name, bucket_name, object_name=None):
        if object_name is None:
            object_name = file_name

        try:
            self.s3_client.upload_file(file_name, bucket_name, object_name)
            print(f"{file_name} has been uploaded to {bucket_name}/{object_name}")
            return
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

if __name__ == "__main__":
    endpoint_url = 'http://localhost:9000'
    aws_secret_access_key = 'your-secret-key'

    s3_repository = S3Repository(endpoint_url)
    
    file_name = 'path/file.txt'
    bucket_name = 'test'
    
    s3_repository.put(file_name, bucket_name)