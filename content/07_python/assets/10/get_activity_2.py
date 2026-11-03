import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3},
)
posts = response.json()

for post in posts:
    print(post["title"])
