import hashlib

target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
common_passwords = ["dragon", "sunshine", "monkey", "password", "football"]

for password in common_passwords:
    if hashlib.sha256(password.encode()).hexdigest() == target_hash:
        print(f"Password found: {password}")
        break
else:
    print("Password not found")
