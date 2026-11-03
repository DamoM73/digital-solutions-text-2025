ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""
    for char in ciphertext.upper():
        if char in ALPHABET:
            position = ALPHABET.index(char)
            new_position = (position - shift) % 26
            plaintext += ALPHABET[new_position]
        else:
            plaintext += char
    return plaintext


ciphertext = "AJESZY TD QFY"

for shift in range(1, 26):
    print(f"{shift:2}: {caesar_decrypt(ciphertext, shift)}")
