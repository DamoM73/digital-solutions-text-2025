ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = ""
    for char in plaintext.upper():
        if char in ALPHABET:
            position = ALPHABET.index(char)
            new_position = (position + shift) % 26
            ciphertext += ALPHABET[new_position]
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)


secret = caesar_encrypt("Digital Solutions", 7)
print(secret)
print(caesar_decrypt(secret, 7))
