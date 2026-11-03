import json

movies = [
    {"title": "Inception", "year": 2010},
    {"title": "The Matrix", "year": 1999},
    {"title": "Interstellar", "year": 2014}
]

with open("movies.json", "w") as file:
    json.dump(movies, file, indent=2)
