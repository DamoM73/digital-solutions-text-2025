import json

contact = {
    "name": "Liam",
    "phone": "0455 123 456",
    "email": "liam@example.com",
    "subscribed": True
}

json_string = json.dumps(contact)
print(json_string)

json_string = json.dumps(contact, indent=4)
print(json_string)
