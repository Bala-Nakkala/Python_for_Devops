import docker
import time

client = docker.from_env()

containers_to_check = ["minikube", "sonarqube", "jenkins"]

print("🔍 Checking container status...\n")

for name in containers_to_check:
    try:
        container = client.containers.get(name)

        print(f"Container: {name}")
        print(f"Status   : {container.status}")

        # If stopped, restart it
        if container.status != "running":
            print(f"⚠️ {name} is not running. Restarting...")
            container.start()
            time.sleep(2)
            container.reload()
            print(f"✅ {name} new status: {container.status}")

        print("-" * 40)

    except docker.errors.NotFound:
        print(f"❌ Container {name} not found")
        print("-" * 40)

    except Exception as e:
        print(f"❌ Error with {name}: {e}")
        print("-" * 40)
        