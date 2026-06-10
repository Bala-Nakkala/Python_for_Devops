import requests

response = requests.get(
    "https://api.github.com/users/Bala-Nakkala/repos"
)

repos = response.json()

for repo in repos:
    print(repo["name"])