import yaml

with open("deployment.yaml", "r") as file:
    data = yaml.safe_load(file)

data["spec"]["replicas"] = 7

with open("deployment.yaml", "w") as file:
    yaml.safe_dump(data, file)

print("Replicas updated successfully")