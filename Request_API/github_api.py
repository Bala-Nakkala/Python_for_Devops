import requests

response = requests.get(
    "https://api.github.com/users/Bala-Nakkala"
)

print("Status Code:", response.status_code)

data = response.json()

print("Username:", data["login"])
print("Public Repos:", data["public_repos"])