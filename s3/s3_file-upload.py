import boto3

s3 = boto3.client("s3")

bucket_name = "balu-0864321"
file_name = "ec2_list.py"
s3_key = "ec2_list.py"

s3.upload_file(file_name, bucket_name, s3_key)

print("File uploaded successfully!")