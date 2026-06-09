import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == "running":
            print("RUNNING Instance:")
            print("ID:", instance["InstanceId"])
            print("Type:", instance["InstanceType"])
            print("-" * 30)