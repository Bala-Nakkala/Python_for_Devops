import requests

try:
    response = requests.get("https://wrong-url.com")
    print(response.status_code)

except Exception as e:
    print("API Call Failed")
    print(e)