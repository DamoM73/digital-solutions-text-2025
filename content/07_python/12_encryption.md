# Encryption

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to code the Caesar, Vigenère, Gronsfeld and one-time pad ciphers in Python
- know how to encrypt and decrypt data with symmetric encryption using the `cryptography` library
- know how to encrypt and decrypt data with asymmetric (RSA) encryption using the `cryptography` library
- know how to store encryption keys safely
:::

:::{note} Resources needed
:class: dropdown
The library examples on this page use the `cryptography` package. With our virtual environment active, install it in the VS Code terminal:

```bash
python -m pip install cryptography
```

Then add `cryptography` to our `requirements.txt` file.
:::

**Encryption** turns readable data (**plaintext**) into unreadable data (**ciphertext**) using a **key**. Only someone with the right key can **decrypt** the ciphertext back into plaintext.

This page is about coding encryption in Python. The theory behind each method, including how it works and how secure it is, is on the [Data Security Management](../05_data_transmission/04_security_management.md#encryption) page.

## Traditional ciphers

Traditional ciphers work on letters. They are far too weak to protect real data, but coding them is a great way to understand how encryption works. All four ciphers below follow the same pattern:

1. find the position of each letter in the alphabet (A = 0, B = 1 … Z = 25)
2. shift that position by the key
3. use `% 26` (modulo 26) so the position wraps around from Z back to A
4. turn the new position back into a letter

### Caesar cipher

The [Caesar cipher](../05_data_transmission/04_security_management.md#caesar-cipher) shifts every letter by the same number of places.

:::{code} python
:linenos:
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


secret = caesar_encrypt("Attack at dawn", 3)
print(secret)
print(caesar_decrypt(secret, 3))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; the alphabet as a string, so we can look up each letter's position. It's in capitals because it is a **constant**: a value that never changes
- **line 6** &rarr; loops through each character of the plaintext, converted to upper case
- **line 7** &rarr; only letters are encrypted. Spaces and punctuation are added unchanged in **line 12**
- **line 8** &rarr; `ALPHABET.index(char)` finds the letter's position, e.g. `"C"` is `2`
- **line 9** &rarr; adds the shift, then `% 26` wraps the result, e.g. `"Y"` (24) + 3 = 27, and 27 % 26 = 1, which is `"B"`
- **line 10** &rarr; adds the new letter to the ciphertext
- **lines 16&ndash;17** &rarr; decrypting is just encrypting with a negative shift. Python's `%` always gives a result from 0 to 25, even for negative numbers
:::

Output:

:::{code} text
DWWDFN DW GDZQ
ATTACK AT DAWN
:::

### Vigenère cipher

The [Vigenère cipher](../05_data_transmission/04_security_management.md#vigen-re-cipher) uses a keyword. Each letter of the keyword gives a different shift, so the same plaintext letter can become different ciphertext letters.

:::{code} python
:linenos:
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_encrypt(plaintext: str, keyword: str) -> str:
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char in ALPHABET:
            shift = ALPHABET.index(keyword[i % len(keyword)])
            new_position = (ALPHABET.index(char) + shift) % 26
            ciphertext += ALPHABET[new_position]
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext: str, keyword: str) -> str:
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in ALPHABET:
            shift = ALPHABET.index(keyword[i % len(keyword)])
            new_position = (ALPHABET.index(char) - shift) % 26
            plaintext += ALPHABET[new_position]
        else:
            plaintext += char
    return plaintext


secret = vigenere_encrypt("Attack at dawn", "lemon")
print(secret)
print(vigenere_decrypt(secret, "lemon"))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 8** &rarr; loops through each position `i` in the plaintext, because we need the position to pick the matching keyword letter
- **line 11** &rarr; `i % len(keyword)` repeats the keyword, so with `"LEMON"` positions 0&ndash;4 use L, E, M, O, N, then position 5 starts again at L. The keyword letter's position in the alphabet is the shift, e.g. `"L"` is a shift of 11
- **line 12** &rarr; shifts the letter forward and wraps it with `% 26`
- **line 27** &rarr; decryption is the same, except the shift is subtracted
:::

Output:

:::{code} text
LXFOPV MH OEIB
ATTACK AT DAWN
:::

:::{hint} Spaces and the keyword
:class: dropdown
Our code matches the Vigenère pseudocode on the Data Security Management page: the keyword moves on one letter for **every** character, including spaces. Many versions of the cipher only move to the next keyword letter after a letter, which gives a different ciphertext (`LXFOPV EF RNHR` for this example). Both work, as long as the sender and receiver use the same method.
:::

### Gronsfeld cipher

The [Gronsfeld cipher](../05_data_transmission/04_security_management.md#gronsfeld-cipher) is the Vigenère cipher with a number for a key. Each digit of the key is the shift for that position.

:::{code} python
:linenos:
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gronsfeld_encrypt(plaintext: str, key: str) -> str:
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char in ALPHABET:
            shift = int(key[i % len(key)])
            new_position = (ALPHABET.index(char) + shift) % 26
            ciphertext += ALPHABET[new_position]
        else:
            ciphertext += char
    return ciphertext


print(gronsfeld_encrypt("Attack at dawn", "31415"))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 4** &rarr; the key is a string of digits, such as `"31415"`, so we can pick out each digit by its position
- **line 10** &rarr; the only change from the Vigenère cipher. Instead of looking up a keyword letter, `int()` turns the digit into the shift
:::

Output:

:::{code} text
DUXBHN EU GBAO
:::

### One-time pad

The [one-time pad](../05_data_transmission/04_security_management.md#one-time-pad-encryption) uses a random key, called the **pad**, that is as long as the message. If the pad is truly random, kept secret and never reused, the cipher can't be broken.

To make the pad, we use Python's `secrets` module. Unlike the `random` module, `secrets` is designed for security, so its values can't be predicted.

:::{code} python
:linenos:
import secrets

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_pad(length: int) -> str:
    pad = ""
    for _ in range(length):
        pad += secrets.choice(ALPHABET)
    return pad


def otp_encrypt(plaintext: str, pad: str) -> str:
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        plain_position = ALPHABET.index(plaintext[i])
        pad_position = ALPHABET.index(pad[i])
        ciphertext += ALPHABET[(plain_position + pad_position) % 26]
    return ciphertext


def otp_decrypt(ciphertext: str, pad: str) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        cipher_position = ALPHABET.index(ciphertext[i])
        pad_position = ALPHABET.index(pad[i])
        plaintext += ALPHABET[(cipher_position - pad_position) % 26]
    return plaintext


message = "ATTACKATDAWN"
pad = generate_pad(len(message))
secret = otp_encrypt(message, pad)
print(f"Pad:        {pad}")
print(f"Ciphertext: {secret}")
print(f"Plaintext:  {otp_decrypt(secret, pad)}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports the `secrets` module for secure random values
- **lines 6&ndash;10** &rarr; builds a pad of random letters. `_` is used as the loop variable because we don't need its value
- **line 9** &rarr; `secrets.choice(ALPHABET)` picks one letter at random
- **lines 17&ndash;19** &rarr; each plaintext letter is shifted by the matching pad letter. Every letter gets its own random shift
- **line 32** &rarr; our version only works with letters, so the message has no spaces
- **line 33** &rarr; makes a new pad that is the same length as the message
:::

Output (the pad and ciphertext will be different every time):

:::{code} text
Pad:        EDFLWEVCHFWB
Ciphertext: EWYLYOVVKFSO
Plaintext:  ATTACKATDAWN
:::

:::{caution} Never reuse a pad
:class: dropdown
The one-time pad is only secure if each pad is used **once**. If two messages are encrypted with the same pad, an attacker can compare the two ciphertexts and start to work out both messages.
:::

## Encryption with the cryptography library

Real encryption algorithms, such as AES and RSA, are very complicated, and small mistakes make them insecure. So the golden rule is: **never write our own encryption for real data**. Instead we use a trusted, well-tested library. In Python, the standard choice is `cryptography`.

### Bytes

Encryption works on **bytes**, not strings. A bytes value looks like a string with a `b` in front of it, such as `b'hello'`.

- `.encode()` &rarr; turns a string into bytes: `"hello".encode()` gives `b'hello'`
- `.decode()` &rarr; turns bytes back into a string: `b'hello'.decode()` gives `"hello"`

So we encode our message before we encrypt it, and decode it after we decrypt it.

### Symmetric encryption with Fernet

[Symmetric encryption](../05_data_transmission/04_security_management.md#symmetric-encryption) uses the same key to encrypt and decrypt. The `cryptography` library's **Fernet** tool does this for us. It uses AES, and also checks that the message hasn't been changed.

:::{code} python
:linenos:
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Key: {key}")

fernet = Fernet(key)

message = "Meet at the library at 3pm"
token = fernet.encrypt(message.encode())
print(f"Encrypted: {token}")

decrypted = fernet.decrypt(token).decode()
print(f"Decrypted: {decrypted}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports the `Fernet` class from the `cryptography` library
- **line 3** &rarr; generates a new random key. The key is bytes
- **line 6** &rarr; creates a `Fernet` object that uses our key
- **line 9** &rarr; encodes the message to bytes, then encrypts it. The encrypted result is called a **token**
- **line 12** &rarr; decrypts the token back to bytes, then decodes it to a string
:::

Output (the key and token will be different every time):

:::{code} text
Key: b'eGQCXAn_a1mWge2O0SrG8dsE1q3MLwNLfsUtSUpF0VU='
Encrypted: b'gAAAAABq6TI2D473x0PtMWe3qqy3Vr4kGaFDBXtiaj0fH1mV3QdyP1_6f3C6S9jI2lqyYcTB7eMJQX1qHeIHhO01vuH0zy3MvFKZ6FWreiq_9yN8eJOBSYA='
Decrypted: Meet at the library at 3pm
:::

If we try to decrypt a token with the wrong key, or a token that has been changed, Fernet raises an `InvalidToken` error. We can catch it with `try` and `except`:

:::{code} python
:linenos:
from cryptography.fernet import Fernet, InvalidToken

fernet = Fernet(Fernet.generate_key())
token = fernet.encrypt("Meet at the library at 3pm".encode())

wrong_fernet = Fernet(Fernet.generate_key())

try:
    print(wrong_fernet.decrypt(token).decode())
except InvalidToken:
    print("Decryption failed: wrong key or the message has been changed")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; also imports the `InvalidToken` error
- **lines 3&ndash;4** &rarr; encrypts a message with one key
- **line 6** &rarr; creates a second `Fernet` object with a different key
- **lines 8&ndash;11** &rarr; tries to decrypt with the wrong key. This raises `InvalidToken`, so the `except` block runs
:::

Output:

:::{code} text
Decryption failed: wrong key or the message has been changed
:::

### Asymmetric encryption with RSA

[Asymmetric encryption](../05_data_transmission/04_security_management.md#asymmetric-encryption) uses a pair of keys. The **public key** encrypts and can be shared with anyone. The **private key** decrypts and must be kept secret. [RSA](../05_data_transmission/04_security_management.md#rsa) is the most widely used asymmetric algorithm.

:::{code} python
:linenos:
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)

message = "My password is hunter2"
ciphertext = public_key.encrypt(message.encode(), oaep)
print(f"Encrypted ({len(ciphertext)} bytes): {ciphertext[:20]}...")

plaintext = private_key.decrypt(ciphertext, oaep).decode()
print(f"Decrypted: {plaintext}")
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 1&ndash;2** &rarr; imports the parts of the library we need for RSA
- **line 4** &rarr; generates a 2048-bit private key. `65537` is the standard value for RSA's public exponent, so we always use it
- **line 5** &rarr; works out the matching public key from the private key
- **lines 7&ndash;11** &rarr; sets up **OAEP padding**. Padding adds random data to the message before it is encrypted, so the same message never gives the same ciphertext. We must use the same padding to encrypt and decrypt
- **line 14** &rarr; encrypts the message with the **public** key
- **line 15** &rarr; prints the size of the ciphertext and its first 20 bytes
- **line 17** &rarr; decrypts the ciphertext with the **private** key
:::

Output (the ciphertext will be different every time):

:::{code} text
Encrypted (256 bytes): b'\x82\xaed0$r\x08q`\x91\xf0\x1c\xcf5+Z\xc8\xd7\xa8\x1a'...
Decrypted: My password is hunter2
:::

:::{hint} RSA and long messages
:class: dropdown
RSA can only encrypt small amounts of data. A 2048-bit key with OAEP padding can encrypt at most 190 bytes. RSA is also much slower than symmetric encryption. So in practice, systems such as HTTPS use RSA to share a symmetric key securely, then use that symmetric key to encrypt the actual data.
:::

## Storing keys safely

Encryption is only as secure as its key. If someone gets our key, they can decrypt everything. So we need to:

- **never hard-code keys** in our Python files
- **never commit keys** to GitHub
- **keep a copy of the key**, because without it our encrypted data is lost for good

### Saving a Fernet key to a file

This program creates a key file once. It won't overwrite an existing key, because that would make anything encrypted with the old key impossible to decrypt.

:::{code} python
:linenos:
from pathlib import Path

from cryptography.fernet import Fernet

key_file = Path("secret.key")

if key_file.exists():
    print("Key already exists. Not overwriting it.")
else:
    key_file.write_bytes(Fernet.generate_key())
    print("New key saved to secret.key")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports `Path`, which makes it easy to read and write files
- **line 5** &rarr; creates a `Path` object for the file **secret.key**
- **lines 7&ndash;8** &rarr; if the key file already exists, leave it alone
- **line 10** &rarr; otherwise, generate a new key and write it to the file as bytes
:::

Then any other program can load the key from the file:

:::{code} python
:linenos:
from pathlib import Path

from cryptography.fernet import Fernet


def load_key() -> bytes:
    return Path("secret.key").read_bytes()


fernet = Fernet(load_key())

token = fernet.encrypt("Our saved key works".encode())
print(fernet.decrypt(token).decode())
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 6&ndash;7** &rarr; reads the key from **secret.key** and returns it as bytes
- **line 10** &rarr; creates a `Fernet` object with the saved key
- **lines 12&ndash;13** &rarr; encrypts and decrypts a message to check the key works
:::

Output:

:::{code} text
Our saved key works
:::

### Saving RSA keys

RSA keys are saved in a standard text format called **PEM**. The public key can be shared, but the private key should be protected with a password.

:::{code} python
:linenos:
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

password = b"use-a-strong-password"

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(password),
)
Path("private_key.pem").write_bytes(private_pem)

public_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
Path("public_key.pem").write_bytes(public_pem)

print("Keys saved")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 3** &rarr; imports `serialization`, which converts keys to and from files
- **line 6** &rarr; the password that protects the private key. In a real app we would ask the user for it rather than writing it in our code
- **line 8** &rarr; generates a new RSA private key
- **lines 10&ndash;14** &rarr; converts the private key to PEM format, encrypted with the password
- **line 15** &rarr; saves the private key to **private_key.pem**
- **lines 17&ndash;20** &rarr; converts the public key to PEM format. It isn't encrypted, because it is meant to be shared
- **line 21** &rarr; saves the public key to **public_key.pem**
:::

To load the keys again, we use `load_pem_private_key()` (with the same password) and `load_pem_public_key()`:

:::{code} python
:linenos:
from pathlib import Path

from cryptography.hazmat.primitives import serialization

password = b"use-a-strong-password"

private_key = serialization.load_pem_private_key(
    Path("private_key.pem").read_bytes(), password=password
)
public_key = serialization.load_pem_public_key(Path("public_key.pem").read_bytes())

print(type(private_key).__name__)
print(type(public_key).__name__)
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 7&ndash;9** &rarr; reads **private_key.pem** and decrypts it with the password
- **line 10** &rarr; reads **public_key.pem**
- **lines 12&ndash;13** &rarr; prints the type of each key to show they loaded correctly
:::

Output:

:::{code} text
RSAPrivateKey
RSAPublicKey
:::

### Keep keys out of GitHub

Our repos are on GitHub, so we must stop Git from uploading our key files. We do this by listing them in the **.gitignore** file in the main folder of our repo. Git ignores any file that matches a line in **.gitignore**.

Add these lines to **.gitignore**:

:::{code} text
secret.key
*.pem
:::

- `secret.key` &rarr; ignores our Fernet key file
- `*.pem` &rarr; ignores every file ending in `.pem`, which covers both RSA key files

:::{danger} Check before we commit
:class: dropdown
If a key has already been committed, adding it to **.gitignore** won't remove it from GitHub. Anyone who can see the repo's history can still find it. If that happens, treat the key as public: generate a new key and re-encrypt anything that used the old one.

Before committing, check the list of changed files in GitHub Desktop and make sure no key files are included.
:::

## Summary

| Task | Code |
| --- | --- |
| Find a letter's position | `ALPHABET.index(char)` |
| Wrap a position around the alphabet | `position % 26` |
| Pick a secure random letter | `secrets.choice(ALPHABET)` |
| String to bytes | `"text".encode()` |
| Bytes to string | `data.decode()` |
| Make a Fernet key | `Fernet.generate_key()` |
| Encrypt with Fernet | `Fernet(key).encrypt(data)` |
| Decrypt with Fernet | `Fernet(key).decrypt(token)` |
| Make an RSA key pair | `rsa.generate_private_key(public_exponent=65537, key_size=2048)` |
| Encrypt with RSA | `public_key.encrypt(data, oaep)` |
| Decrypt with RSA | `private_key.decrypt(ciphertext, oaep)` |
| Save a key to a file | `Path("secret.key").write_bytes(key)` |
| Load a key from a file | `Path("secret.key").read_bytes()` |

:::{seealso} Encryption Activities
:class: dropdown
**Activity 1: Caesar cipher**

Use the `caesar_encrypt()` and `caesar_decrypt()` functions from this page to encrypt `"Digital Solutions"` with a shift of 7, then decrypt it.

Expected Output:

```text
KPNPAHS ZVSBAPVUZ
DIGITAL SOLUTIONS
```

---

**Activity 2: Brute force a Caesar cipher**

The Caesar cipher only has 25 possible shifts, so we can try them all. This is called a **brute force attack**.

Write a program that decrypts the ciphertext below with every shift from 1 to 25 and prints each result. Which shift reveals the message?

```text
AJESZY TD QFY
```

Expected Output (first three of 25 lines):

```text
 1: ZIDRYX SC PEX
 2: YHCQXW RB ODW
 3: XGBPWV QA NCV
```

---

**Activity 3: Gronsfeld decryption**

Write a `gronsfeld_decrypt()` function, then use it to decrypt this ciphertext with the key `"2718"`.

```text
GUDZAWU CSM VOF VOJVIZ
```

Expected Output:

```text
ENCRYPT ALL THE THINGS
```

---

**Activity 4: Save an encrypted message**

Write a program that:

1. loads the Fernet key from **secret.key**, or creates the file if it doesn't exist
2. asks the user for a message and encrypts it
3. saves the token to a file called **message.txt**
4. reads **message.txt** back, decrypts the token and prints the message

Then add **secret.key** to our **.gitignore** file.

Expected Output (when the user enters `Hello Bob`):

```text
Enter a message to encrypt: Hello Bob
Encrypted message saved to message.txt
Decrypted: Hello Bob
```

---

**Activity 5: Only the private key works**

Write a program that:

1. creates an RSA key pair for Alice and a separate key pair for Bob
2. encrypts `"Year 11 Digital Solutions"` with Alice's **public** key
3. decrypts the message with Alice's **private** key and prints it
4. tries to decrypt the message with Bob's private key. RSA raises a `ValueError` when the wrong key is used, so catch it and print a message

Expected Output:

```text
Alice decrypts: Year 11 Digital Solutions
Bob can't decrypt the message
```
:::
