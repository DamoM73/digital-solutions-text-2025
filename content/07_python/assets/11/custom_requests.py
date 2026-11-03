import requests

BASE_URL = "http://127.0.0.1:8000/api/"


def call_api(function_name: str, arguments: dict) -> list:
    response = requests.get(BASE_URL + function_name, params=arguments)
    response.raise_for_status()
    return response.json()["results"]


def show(title: str, results: list) -> None:
    print(title)
    for row in results:
        print("   ", ", ".join(str(value) for value in row.values()))
    print()


show("1. Number of tracks", call_api("track_count", {}))
show("2. Five most expensive tracks", call_api("most_expensive_tracks", {}))
show("3. Tracks per genre", call_api("genre_counts", {}))
show("4. Sales Support Agents", call_api("sales_support_agents", {}))
show("5. Best selling track", call_api("best_selling_track", {}))
show("6. Customers in Australia", call_api("customers_in_country", {"country": "Australia"}))
show("7. Tracks longer than 20 minutes", call_api("tracks_longer_than", {"seconds": 1200})[:5])
show("8. Albums by Queen", call_api("artist_albums", {"artist": "Queen"}))
show("9. Invoices from Australia", call_api("country_invoices", {"country": "Australia"}))
show("10. Total spent by customer 55", call_api("customer_total_spent", {"customer_id": 55}))
