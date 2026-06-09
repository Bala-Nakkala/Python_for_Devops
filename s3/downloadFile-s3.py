import boto3

s3 = boto3.client("s3")

bucket_name = "balu-0864321"
file_key = "ec2_list.py"

s3.delete_object(Bucket=bucket_name, Key=file_key)

print("File deleted from S3 successfully!")