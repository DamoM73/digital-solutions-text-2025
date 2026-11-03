import json

json_data = '{"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "available": true}'

book = json.loads(json_data)

print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Year: {book['year']}")
print(f"Available: {book['available']}")
