import boto3

def get_ec2_inventory():
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    instances_data = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instance_id = instance.get("InstanceId")
            state = instance["State"]["Name"]
            instance_type = instance.get("InstanceType")
            private_ip = instance.get("PrivateIpAddress", "N/A")

            # Get Name tag
            name = "No Name"
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]

            instances_data.append({
                "Name": name,
                "InstanceId": instance_id,
                "State": state,
                "Type": instance_type,
                "PrivateIP": private_ip
            })

    return instances_data


def print_inventory(data):
    print("\nEC2 INVENTORY REPORT")
    print("=" * 50)

    for inst in data:
        print(f"Name        : {inst['Name']}")
        print(f"Instance ID : {inst['InstanceId']}")
        print(f"State       : {inst['State']}")
        print(f"Type        : {inst['Type']}")
        print(f"Private IP  : {inst['PrivateIP']}")
        print("-" * 50)


if __name__ == "__main__":
    data = get_ec2_inventory()
    print_inventory(data)