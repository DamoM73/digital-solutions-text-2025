import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")

try:
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError:
    if response.status_code == 404:
        print("Error: The requested post was not found (404).")
    else:
        print(f"Error: The server returned {response.status_code}.")
