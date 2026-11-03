import requests

BASE_URL = "http://127.0.0.1:8000/api/"

# each API function and the arguments it needs
functions = {
    "country_info_brief": {"country": "Brazil"},
    "country_info": {"country": "Brazil"},
    "list_countries": {},
    "country_continent": {"country": "Brazil"},
    "pop_greater": {"min_pop": 200000000},
    "continent_countries": {"continent": "South America"},
    "continent_countries_pop_greater": {"continent": "South America", "min_pop": 40000000},
    "vets_list": {},
    "add_vet": {
        "first_name": "Priya",
        "last_name": "Sharma",
        "phone": "0477777777",
        "address": "12 Bay St",
        "room": 104,
        "appointment_times": "Mon - Wed, 9:00-15:00",
        "email": "priya@example.com",
    },
    "delete_vet": {"first_name": "Priya", "last_name": "Sharma"},
}

for name, arguments in functions.items():
    # GET request: arguments are sent in the URL
    get_response = requests.get(BASE_URL + name, params=arguments)
    print(f"GET  {name}: {get_response.status_code} {get_response.text[:70]}")

    # POST request: arguments are sent in the body of the request
    post_response = requests.post(BASE_URL + name, data=arguments)
    print(f"POST {name}: {post_response.status_code} {post_response.text[:70]}")
