import docker

client = docker.from_env()

print("Docker connected successfully")
print(client.version())