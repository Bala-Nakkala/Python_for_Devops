import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.delete_alarms(
    AlarmNames=["HighCPUAlarm"]
)

print("Alarm deleted successfully")