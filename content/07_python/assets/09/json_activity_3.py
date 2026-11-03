import json

with open("car.json", "r") as file:
    car = json.load(file)

print(f"Make: {car['make']}")
print(f"Model: {car['model']}")
print(f"Year: {car['year']}")
print(f"Electric: {car['electric']}")
