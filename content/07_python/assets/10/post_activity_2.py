import requests

new_comment = {
    "name": "Great post",
    "email": "student@example.com",
    "postId": 1,
    "body": "Thanks, this helped me understand APIs.",
}

response = requests.post("https://jsonplaceholder.typicode.com/comments", json=new_comment)
comment = response.json()
print(f"New comment ID: {comment['id']}")
