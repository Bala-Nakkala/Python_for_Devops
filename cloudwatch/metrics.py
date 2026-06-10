import boto3

cloudwatch = boto3.client("cloudwatch")

response = cloudwatch.list_metrics(
    Namespace="AWS/EC2"
)

print(response["Metrics"][:5])