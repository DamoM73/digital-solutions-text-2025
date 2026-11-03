import requests

headers = {"Authorization": "Bearer abc123"}

response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())
