import requests

response = requests.get("http://127.0.0.1:8000/api/list_countries")
countries = response.json()["results"]

for country in countries:
    print(f"{country['name']}: capital {country['capital']}, population {country['population']:,.0f}")
