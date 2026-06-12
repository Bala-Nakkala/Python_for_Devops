from kubernetes import client, config

config.load_kube_config()

apps_v1 = client.AppsV1Api()

deployment_name = "nginx-deployment"
namespace = "default"

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
    namespace=namespace,
    body=body
)

print("✅ Deployment restarted")