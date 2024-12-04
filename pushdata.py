import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os


load_dotenv()


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = "dataengineeringprojbucket"
FILE_PATH = "../../Downloads/data.csv"
FOLDER_NAME = "raw" 
S3_FILE_NAME = f"{FOLDER_NAME}/uploaded_data.csv"  

def upload_file_to_s3(file_path, bucket_name, s3_file_name):
    try:

        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

        s3_client.upload_file(file_path, bucket_name, s3_file_name)
        print(f"File '{file_path}' successfully uploaded to '{bucket_name}/{s3_file_name}'.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
upload_file_to_s3(FILE_PATH, BUCKET_NAME, S3_FILE_NAME)