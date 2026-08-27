from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

print("\n☸️ CLUSTER INFO\n")

nodes = v1.list_node()

for node in nodes.items:
    print("Node Name:", node.metadata.name)

    for condition in node.status.conditions:
        if condition.type == "Ready":
            print("Status:", condition.status)
            break

    print("-" * 30)