import boto3

iam = boto3.client("iam")

user_name = "Bala"  # change this

response = iam.list_attached_user_policies(UserName=user_name)

print(f"\nPOLICIES FOR USER: {user_name}")
print("=" * 50)

for policy in response["AttachedPolicies"]:
    print("Policy Name:", policy["PolicyName"])
    print("Policy ARN :", policy["PolicyArn"])
    print("-" * 40)