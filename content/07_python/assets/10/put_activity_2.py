import requests

updated_user = {
    "id": 5,
    "name": "Alex Taylor",
    "username": "alext",
    "email": "alex.taylor@example.com",
    "phone": "0412 345 678",
    "website": "alextaylor.example.com",
}

response = requests.put("https://jsonplaceholder.typicode.com/users/5", json=updated_user)

if response.status_code == 200:
    print(f"User {response.json()['id']} was updated")
else:
    print(f"Update failed: {response.status_code}")
