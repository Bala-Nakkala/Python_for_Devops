import boto3

ec2 = boto3.client("ec2")

instance_id = "i-0c0dcbea21fbc1fe1"  # change this

response = ec2.start_instances(
    InstanceIds=[instance_id]
)

print("Starting EC2 instance...")
print(response)