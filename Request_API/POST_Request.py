import requests

data = {
    "name": "Balu"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print(response.json())
else:
    print("Request Failed")
    print(response.text)