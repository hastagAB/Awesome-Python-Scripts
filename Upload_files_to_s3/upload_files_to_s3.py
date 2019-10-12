import boto3
import os

ACL = 'public-read' #access type of the file
AWS_ACCESS_KEY_ID = 'your_access_key'
AWS_REGION = 'your_region'
AWS_SECRET_ACCESS_KEY = 'your_secret_key'
AWS_STORAGE_BUCKET_NAME = 'my_bucket'
FOLDER_NAME_ON_S3 = 'my_folder_on_s3'
FOLDER_PATH = '/home/foo/my_folder'


def upload_files_to_s3(path):
    """
    Upload files to AWS s3 bucket from your machine
    using python and boto3
    """    
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                key = FOLDER_NAME_ON_S3 + full_path[len(path) + 1:]
                bucket.put_object(Key=key, Body=data, ACL=ACL)

if __name__ == "__main__":
    upload_files_to_s3(FOLDER_PATH)