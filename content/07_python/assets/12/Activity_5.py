from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)

alice_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
alice_public = alice_private.public_key()

bob_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)

ciphertext = alice_public.encrypt("Year 11 Digital Solutions".encode(), oaep)

print(f"Alice decrypts: {alice_private.decrypt(ciphertext, oaep).decode()}")

try:
    bob_private.decrypt(ciphertext, oaep)
except ValueError:
    print("Bob can't decrypt the message")
