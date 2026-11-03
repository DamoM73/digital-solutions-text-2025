import json

with open("inventory.json", "r") as file:
    inventory = json.load(file)

for item in inventory:
    print(f"{item['item']}: {item['stock']}")
