from file_transfer.file_manager import scan_files
from file_transfer.aws_uploader import upload_to_s3
from file_transfer.gcs_uploader import upload_to_gcs
from file_transfer.config import AWS_S3_BUCKET, GCS_BUCKET


def main():
    directory = input("Enter the directory path: ")
    files_to_upload = scan_files(directory)

    for file in files_to_upload['images'] + files_to_upload['media']:
        upload_to_s3(file, AWS_S3_BUCKET)

    for file in files_to_upload['documents']:
        upload_to_gcs(file, GCS_BUCKET)


if __name__ == "__main__":
    main()
