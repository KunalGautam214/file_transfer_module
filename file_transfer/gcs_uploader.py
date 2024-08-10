from google.cloud import storage
import os

def upload_to_gcs(file_path, bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    try:
        file_name = os.path.basename(file_path)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_name} to GCS bucket {bucket_name}")
    except Exception as e:
        print(f"Failed to upload {file_path} to GCS: {str(e)}")
