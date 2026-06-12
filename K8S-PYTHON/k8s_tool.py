from kubernetes import client, config
import sys

config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()


# ---------------- CLUSTER ----------------
def cluster_info():
    print("\n☸️ CLUSTER INFO\n")
    nodes = v1.list_node()
    for node in nodes.items:
        print(node.metadata.name, "→", node.status.conditions[-1].type)


# ---------------- PODS ----------------
def pod_status():
    print("\n📦 POD STATUS (default namespace)\n")
    pods = v1.list_namespaced_pod("default")
    for pod in pods.items:
        print(pod.metadata.name, "→", pod.status.phase)


# ---------------- RESTART POD ----------------
def restart_pod(pod_name):
    print(f"\n🔁 Restarting pod: {pod_name}")
    v1.delete_namespaced_pod(name=pod_name, namespace="default")
    print("✅ Pod deleted (will auto-recreate)")


# ---------------- RESTART DEPLOYMENT ----------------
def restart_deployment(deployment_name):
    print(f"\n🔄 Restarting deployment: {deployment_name}")

    body = {
        "spec": {
            "template": {
                "metadata": {
                    "annotations": {
                        "kubectl.kubernetes.io/restartedAt": "now"
                    }
                }
            }
        }
    }

    apps_v1.patch_namespaced_deployment(
        name=deployment_name,
        namespace="default",
        body=body
    )

    print("✅ Deployment restarted")


# ---------------- MAIN ----------------
if len(sys.argv) < 2:
    print("""
Usage:
  python3 k8s_tool.py cluster
  python3 k8s_tool.py pods
  python3 k8s_tool.py restart-pod <pod>
  python3 k8s_tool.py restart-deployment <deployment>
""")
    sys.exit()

cmd = sys.argv[1]

if cmd == "cluster":
    cluster_info()

elif cmd == "pods":
    pod_status()

elif cmd == "restart-pod":
    restart_pod(sys.argv[2])

elif cmd == "restart-deployment":
    restart_deployment(sys.argv[2])

else:
    print("Invalid command")