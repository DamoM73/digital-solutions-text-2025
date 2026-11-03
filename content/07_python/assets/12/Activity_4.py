from pathlib import Path

from cryptography.fernet import Fernet

key_file = Path("secret.key")
if not key_file.exists():
    key_file.write_bytes(Fernet.generate_key())

fernet = Fernet(key_file.read_bytes())

message = input("Enter a message to encrypt: ")
token = fernet.encrypt(message.encode())
Path("message.txt").write_bytes(token)
print("Encrypted message saved to message.txt")

saved_token = Path("message.txt").read_bytes()
print(f"Decrypted: {fernet.decrypt(saved_token).decode()}")
