import boto3
import os

def upload_to_s3(file_path, bucket_name):
    s3_client = boto3.client('s3')
    try:
        file_name = os.path.basename(file_path)
        s3_client.upload_file(file_path, bucket_name, file_name)
        print(f"Uploaded {file_name} to S3 bucket {bucket_name}")
    except Exception as e:
        print(f"Failed to upload {file_path} to S3: {str(e)}")
