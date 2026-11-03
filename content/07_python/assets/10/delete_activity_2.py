import requests

response = requests.delete("https://jsonplaceholder.typicode.com/comments/7")

if response.status_code in (200, 204):
    print("Comment deleted")
else:
    print(f"Delete failed: {response.status_code}")
