from datastore import Datastore

db = Datastore("data/users.db")

print(db.change_password("alex", "wrong-password", "N3w-Passw0rd!"))
print(db.change_password("alex", "password123", "N3w-Passw0rd!"))
print(db.check_login("alex", "password123"))
print(db.check_login("alex", "N3w-Passw0rd!"))
