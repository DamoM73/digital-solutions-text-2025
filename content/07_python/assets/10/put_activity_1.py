import requests

updated_post = {
    "id": 1,
    "title": "A brand new title",
    "body": "A brand new body.",
    "userId": 2,
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
print(response.json())
