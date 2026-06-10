import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_security_groups()

print("\nSECURITY GROUP AUDIT")
print("=" * 60)

for sg in response["SecurityGroups"]:

    sg_name = sg["GroupName"]
    sg_id = sg["GroupId"]

    for rule in sg["IpPermissions"]:

        port = rule.get("FromPort", "All")

        for ip_range in rule.get("IpRanges", []):

            if ip_range["CidrIp"] == "0.0.0.0/0":

                print(f"Security Group : {sg_name}")
                print(f"SG ID          : {sg_id}")
                print(f"Port           : {port}")
                print(f"Source         : 0.0.0.0/0")
                print("-" * 60)