import requests

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/2",
    json={"title": "An updated title"},
)
print(response.json())
