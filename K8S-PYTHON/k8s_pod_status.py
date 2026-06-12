from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

print("\n📦 POD STATUS (default namespace)\n")

pods = v1.list_namespaced_pod("default")

for pod in pods.items:
    print(pod.metadata.name, "→", pod.status.phase)