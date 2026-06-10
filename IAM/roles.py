import boto3

iam = boto3.client("iam")

response = iam.list_roles()

print("\nIAM ROLES")
print("=" * 40)

for role in response["Roles"]:
    print("Role Name:", role["RoleName"])
    print("Created  :", role["CreateDate"])
    print("-" * 40)