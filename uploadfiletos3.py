import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_to_s3(file_name, bucket, object_name=None, region="ap-south-1"):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :param region: AWS region where the bucket is located
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Create an S3 client
    s3_client = boto3.client('s3', region_name=region)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
        return True
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    file_name = 'C:\\Users\\nayan.tank\\Desktop\\abc.jpg'  # Replace with your file path
    bucket_name = 'new-finger-tips'  # Replace with your S3 bucket name
    region_name = 'ap-south-1'  # Replace with your bucket's region

    upload_to_s3(file_name, bucket_name, region=region_name)
