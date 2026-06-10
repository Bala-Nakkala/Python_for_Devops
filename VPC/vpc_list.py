import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_vpcs()

for vpc in response["Vpcs"]:
    print("VPC ID:", vpc["VpcId"])
    print("CIDR :", vpc["CidrBlock"])
    print("-" * 30)