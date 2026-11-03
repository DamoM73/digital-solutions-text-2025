import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/10")
print(response.status_code)
