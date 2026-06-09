import boto3

ec2 = boto3.client("ec2")

instance_id = "i-0abc123456789"  # change this

response = ec2.stop_instances(
    InstanceIds=["i-0c0dcbea21fbc1fe1"]
)

print("Stopping EC2 instance...")
print(response)