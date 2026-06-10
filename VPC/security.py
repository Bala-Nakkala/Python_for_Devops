import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print("SG Name:", sg["GroupName"])
    print("SG ID  :", sg["GroupId"])
    print("-" * 30)