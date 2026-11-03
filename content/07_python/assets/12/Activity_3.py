ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gronsfeld_decrypt(ciphertext: str, key: str) -> str:
    ciphertext = ciphertext.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in ALPHABET:
            shift = int(key[i % len(key)])
            new_position = (ALPHABET.index(char) - shift) % 26
            plaintext += ALPHABET[new_position]
        else:
            plaintext += char
    return plaintext


print(gronsfeld_decrypt("GUDZAWU CSM VOF VOJVIZ", "2718"))
