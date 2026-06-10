import boto3

iam = boto3.client("iam")

response = iam.list_users()

print("\nIAM USERS LIST")
print("=" * 40)

for user in response["Users"]:
    print("User Name :", user["UserName"])
    print("User ID   :", user["UserId"])
    print("Created On:", user["CreateDate"])
    print("-" * 40)