import docker

client = docker.from_env()

containers = client.containers.list()

if not containers:
    print("No running containers")
else:
    print("Running containers:\n")
    for c in containers:
        print(f"Name: {c.name}")
        print(f"Image: {c.image.tags}")
        print(f"Status: {c.status}")
        print("-" * 30)