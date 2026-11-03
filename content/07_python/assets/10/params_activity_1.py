import requests

params = {"userId": 5}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

for post in response.json():
    print(post["title"])
