import docker
import time

client = docker.from_env()

containers_to_stop = ["minikube", "sonarqube", "jenkins"]

print("🛑 Stopping containers...\n")

for name in containers_to_stop:
    try:
        container = client.containers.get(name)

        print(f"Container: {name}")
        print(f"Current Status: {container.status}")

        if container.status == "running":
            print(f"⏹️ Stopping {name}...")
            container.stop()
            time.sleep(2)
            container.reload()
            print(f"✅ {name} stopped successfully. Status: {container.status}")
        else:
            print(f"ℹ️ {name} is already not running.")

        print("-" * 40)

    except docker.errors.NotFound:
        print(f"❌ Container {name} not found")
        print("-" * 40)

    except Exception as e:
        print(f"❌ Error stopping {name}: {e}")
        print("-" * 40)