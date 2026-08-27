import boto3
import csv

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

# CSV file name
csv_file = "ec2_inventory.csv"

# CSV headers
headers = ["Name", "InstanceId", "State", "Type", "PrivateIP"]

rows = []

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        instance_id = instance.get("InstanceId", "N/A")
        state = instance["State"]["Name"]
        instance_type = instance.get("InstanceType", "N/A")
        private_ip = instance.get("PrivateIpAddress", "N/A")

        # Get Name tag
        name = "No Name"
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]

        rows.append([
            name,
            instance_id,
            state,
            instance_type,
            private_ip
        ])

# Write to CSV
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"\nEC2 Inventory exported successfully to {csv_file}")