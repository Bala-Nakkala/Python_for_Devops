import docker
import time

client = docker.from_env()

containers_to_monitor = ["minikube", "sonarqube", "jenkins"]

print("🩺 Starting Auto-Healing Monitor...\n")

for name in containers_to_monitor:
    try:
        container = client.containers.get(name)

        container.reload()  # get latest status

        print(f"Container: {name}")
        print(f"Status   : {container.status}")

        # AUTO-HEAL LOGIC
        if container.status != "running":
            print(f"⚠️ {name} is down! Restarting...")

            container.start()
            time.sleep(2)

            container.reload()

            print(f"✅ {name} healed. New status: {container.status}")

        else:
            print(f"✔️ {name} is healthy")

        print("-" * 40)

    except docker.errors.NotFound:
        print(f"❌ Container {name} not found")
        print("-" * 40)

    except Exception as e:
        print(f"❌ Error with {name}: {e}")
        print("-" * 40)