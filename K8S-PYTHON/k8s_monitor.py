from kubernetes import client, config
import time
import sys
from datetime import datetime

config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()


# ---------------- LOGGING ----------------
def log(msg):
    print(f"[{datetime.now()}] {msg}")


# ---------------- POD HEALTH CHECK ----------------
def check_pods():
    log("Checking pod health...\n")

    pods = v1.list_namespaced_pod("default")

    failed = []

    for pod in pods.items:
        name = pod.metadata.name
        status = pod.status.phase

        if status != "Running":
            log(f"❌ {name} → {status}")
            failed.append(name)
        else:
            log(f"✔ {name} → {status}")

    return failed


# ---------------- HEAL (RESTART FAILED PODS) ----------------
def heal_pods(failed_pods):
    log("\nHealing failed pods...\n")

    for pod in failed_pods:
        try:
            v1.delete_namespaced_pod(name=pod, namespace="default")
            log(f"🔁 Restarted pod: {pod}")
        except Exception as e:
            log(f"⚠️ Failed to restart {pod}: {e}")


# ---------------- WATCH MODE ----------------
def watch_mode():
    log("Starting continuous monitoring (every 10 sec)...\n")

    while True:
        failed = check_pods()

        if len(failed) > 0:
            log(f"⚠️ Found {len(failed)} failed pods")

        time.sleep(10)


# ---------------- ONCE CHECK ----------------
def once_mode():
    failed = check_pods()

    if failed:
        log("\n⚠️ Failed pods detected")
    else:
        log("\n✅ All pods healthy")


# ---------------- HEAL MODE ----------------
def heal_mode():
    failed = check_pods()

    if failed:
        heal_pods(failed)
    else:
        log("✅ No issues found")


# ---------------- MAIN ----------------
if len(sys.argv) < 2:
    print("""
Usage:
  python3 k8s_monitor.py once
  python3 k8s_monitor.py watch
  python3 k8s_monitor.py heal
""")
    sys.exit()

cmd = sys.argv[1]

if cmd == "once":
    once_mode()

elif cmd == "watch":
    watch_mode()

elif cmd == "heal":
    heal_mode()

else:
    print("Invalid command")