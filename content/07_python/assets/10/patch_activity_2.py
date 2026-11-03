import requests

response = requests.patch(
    "https://jsonplaceholder.typicode.com/users/3",
    json={"email": "new.email@example.com"},
)
print(response.json())
