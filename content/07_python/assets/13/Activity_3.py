import hashlib
import secrets

ITERATIONS = 600_000


def hash_new_password(password: str) -> tuple[bytes, bytes]:
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
    return salt, password_hash


for _ in range(3):
    salt, password_hash = hash_new_password("letmein")
    print(f"salt: {salt.hex()}  hash: {password_hash.hex()[:16]}...")
