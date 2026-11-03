import requests

try:
    response = requests.get("https://httpbin.org/delay/5", timeout=2)
    print(response.json())
except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")
