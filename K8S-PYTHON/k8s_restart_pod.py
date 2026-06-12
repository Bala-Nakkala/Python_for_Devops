from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

pod_name = "nginx-deployment-6f9664446b-gx7km"
namespace = "default"

print(f"\n🔁 Restarting pod: {pod_name}")

v1.delete_namespaced_pod(name=pod_name, namespace=namespace)

print("✅ Pod deleted, Kubernetes will recreate it automatically")