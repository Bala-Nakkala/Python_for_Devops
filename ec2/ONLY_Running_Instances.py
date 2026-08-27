import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"]
        }
    ]
)

print("\nRUNNING EC2 INSTANCES")
print("=" * 50)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        print("Instance ID :", instance["InstanceId"])
        print("Type        :", instance.get("InstanceType"))
        print("State       :", instance["State"]["Name"])
        print("-" * 40)