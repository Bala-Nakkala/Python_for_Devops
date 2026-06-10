import boto3

iam = boto3.client("iam")

response = iam.list_users()

print("\nUSERS WITH ADMIN ACCESS")
print("=" * 50)

for user in response["Users"]:
    user_name = user["UserName"]

    policies = iam.list_attached_user_policies(UserName=user_name)

    for policy in policies["AttachedPolicies"]:
        if policy["PolicyName"] == "AdministratorAccess":
            print("ADMIN USER FOUND:")
            print("User Name :", user_name)
            print("Policy    :", policy["PolicyName"])
            print("-" * 40)