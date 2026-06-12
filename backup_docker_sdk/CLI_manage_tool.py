import docker
import sys
import time

client = docker.from_env()


def list_containers():
    print("\n📋 All Containers:\n")
    containers = client.containers.list(all=True)

    for c in containers:
        print(f"{c.name} → {c.status}")


def get_container(name):
    try:
        return client.containers.get(name)
    except:
        print(f"❌ Container '{name}' not found")
        sys.exit(1)


def start(name):
    c = get_container(name)
    c.start()
    time.sleep(1)
    c.reload()
    print(f"▶️ {name} started → {c.status}")


def stop(name):
    c = get_container(name)
    c.stop()
    time.sleep(1)
    c.reload()
    print(f"🛑 {name} stopped → {c.status}")


def restart(name):
    c = get_container(name)
    c.restart()
    time.sleep(1)
    c.reload()
    print(f"🔁 {name} restarted → {c.status}")


def status(name):
    c = get_container(name)
    c.reload()
    print(f"{name} → {c.status}")


def help_menu():
    print("""
Usage:
  python3 smart_container_tool.py list
  python3 smart_container_tool.py start <name>
  python3 smart_container_tool.py stop <name>
  python3 smart_container_tool.py restart <name>
  python3 smart_container_tool.py status <name>
""")


# ================= MAIN LOGIC ================= #

if len(sys.argv) == 1:
    list_containers()
    sys.exit()

action = sys.argv[1]

if action == "list":
    list_containers()

elif action == "start" and len(sys.argv) == 3:
    start(sys.argv[2])

elif action == "stop" and len(sys.argv) == 3:
    stop(sys.argv[2])

elif action == "restart" and len(sys.argv) == 3:
    restart(sys.argv[2])

elif action == "status" and len(sys.argv) == 3:
    status(sys.argv[2])

else:
    help_menu()