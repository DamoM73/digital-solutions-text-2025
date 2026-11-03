# Hashing

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to hash data in Python using the `hashlib` module
- understand why hashing is one-way, and why a small change gives a completely different hash
- know how to hash passwords safely using a salt and `pbkdf2_hmac`
- know how to store hashed passwords in a SQLite database and check a login
:::

A **hash function** turns data of any size into a fixed-size value called a **hash** (or **digest**). It's like a fingerprint for the data. The theory behind hashing is on the [Data Security Management](../05_data_transmission/04_security_management.md#hashing) page.

Hashing is different from [encryption](./12_encryption.md):

- **encryption** is two-way &rarr; with the key, we can decrypt the ciphertext back to the plaintext
- **hashing** is one-way &rarr; there is no key, and we can't turn a hash back into the original data

All the hashing tools on this page are built into Python, so there is nothing to install.

## Hashing with hashlib

Python's built-in `hashlib` module provides the common hash functions. We'll use **SHA-256**, which always produces a 256-bit hash.

:::{code} python
:linenos:
import hashlib

message = "Digital Solutions"
hash_object = hashlib.sha256(message.encode())
digest = hash_object.hexdigest()

print(digest)
print(len(digest))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports Python's built-in `hashlib` module
- **line 4** &rarr; hash functions work on bytes, so `.encode()` turns the string into bytes before `hashlib.sha256()` hashes it
- **line 5** &rarr; `hexdigest()` gives the hash as a string of **hexadecimal** characters (0&ndash;9 and a&ndash;f), which is easy to print and store
- **line 8** &rarr; prints the length of the hash
:::

Output:

:::{code} text
9219a0a8f1ef2067f908bf6e786532b490265bb0b7415166e9c182e1b75336ab
64
:::

A SHA-256 hash is always 64 hexadecimal characters long, whether we hash one letter or a whole book.

### Properties of a hash

Let's put our hashing code into a function and test it:

:::{code} python
:linenos:
import hashlib


def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


print(sha256_hash("Hello"))
print(sha256_hash("Hello"))
print(sha256_hash("hello"))
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 4&ndash;5** &rarr; a function that takes a string and returns its SHA-256 hash as a hexadecimal string
- **lines 8&ndash;9** &rarr; hashes `"Hello"` twice
- **line 10** &rarr; hashes `"hello"`, which only differs by a lower-case `h`
:::

Output:

:::{code} text
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
:::

This shows the two properties that make hashing useful:

- **deterministic** &rarr; the same input always gives the same hash. That's why the first two lines match
- **avalanche effect** &rarr; a tiny change to the input gives a completely different hash. Changing one letter changed the whole hash, not just one character

:::{hint} Other hash functions
:class: dropdown
`hashlib` includes other hash functions, such as `md5()`, `sha1()` and `sha512()`. They all work the same way. MD5 and SHA-1 are older and are now considered broken for security, so we use SHA-256 or stronger.
:::

## Hashing passwords

A system should **never store passwords as plain text**. If the database is stolen, every user's password is exposed, and because people reuse passwords, their other accounts are exposed too.

Instead, a system stores a hash of each password. When a user logs in, the system hashes the password they type and compares it with the stored hash. If the hashes match, the password was correct, but the real password is never stored.

### Why SHA-256 isn't enough

We might think we can just store the SHA-256 hash of each password. Let's see what happens when two users choose the same password:

:::{code} python
:linenos:
import hashlib

users: dict[str, str] = {}

users["alex"] = hashlib.sha256("password123".encode()).hexdigest()
users["sam"] = hashlib.sha256("password123".encode()).hexdigest()

for username, password_hash in users.items():
    print(f"{username}: {password_hash}")
:::

Output:

:::{code} text
alex: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
sam: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
:::

The hashes are identical. This causes two problems:

1. **Matching hashes give passwords away.** An attacker who cracks one hash knows the password of everyone with the same hash.
2. **SHA-256 is too fast.** A computer can calculate billions of SHA-256 hashes every second. Attackers hash huge lists of common passwords and compare the results with stolen hashes. They also use **rainbow tables**: huge lists of passwords that have already been hashed.

### Salting

The fix for matching hashes is a **salt**: a random value that is added to the password before it is hashed. Every user gets a different salt, so even identical passwords give different hashes. The salt isn't secret. It is stored next to the hash, because we need it again to check the password.

### Slow hashing with pbkdf2_hmac

The fix for fast hashing is a **key derivation function**, a hash function that is designed to be slow. `hashlib.pbkdf2_hmac()` runs the hash over and over, as many times as we tell it to. One login only takes a fraction of a second, but an attacker trying billions of passwords is slowed down enormously.

:::{code} python
:linenos:
import hashlib
import secrets

ITERATIONS = 600_000


def hash_password(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)


alex_salt = secrets.token_bytes(16)
sam_salt = secrets.token_bytes(16)

print(f"alex: {hash_password('password123', alex_salt).hex()}")
print(f"sam:  {hash_password('password123', sam_salt).hex()}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 2** &rarr; imports the `secrets` module, which makes secure random values
- **line 4** &rarr; the number of times to repeat the hash. 600,000 is the number OWASP (a respected web security organisation) currently recommends for PBKDF2 with SHA-256. The `_` in `600_000` just makes the number easier to read
- **lines 7&ndash;8** &rarr; hashes the password with SHA-256, using the salt, `ITERATIONS` times. The result is bytes
- **lines 11&ndash;12** &rarr; `secrets.token_bytes(16)` makes a random 16-byte salt for each user
- **lines 14&ndash;15** &rarr; hashes the same password with each salt. `.hex()` turns the bytes into a hexadecimal string so we can print it
:::

Output (the hashes will be different every time, because the salts are random):

:::{code} text
alex: ce855f9fe784c6ea961f63bf069729e6182b2cb36c3c9b62a8c3b453ea64598f
sam:  ac885a0f2917655fa83253dca704e6c2edd286cac409d25ab6ac9cb5fda0f6c1
:::

Same password, different hashes. We'll notice the program takes a moment to run. That delay is deliberate.

### Checking a password

To check a password, we hash it again with the user's stored salt and compare it to the stored hash.

:::{code} python
:linenos:
import hashlib
import hmac
import secrets

ITERATIONS = 600_000


def hash_password(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)


def verify_password(password: str, salt: bytes, stored_hash: bytes) -> bool:
    new_hash = hash_password(password, salt)
    return hmac.compare_digest(new_hash, stored_hash)


salt = secrets.token_bytes(16)
stored_hash = hash_password("correct horse battery staple", salt)

print(verify_password("correct horse battery staple", salt, stored_hash))
print(verify_password("Correct horse battery staple", salt, stored_hash))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 2** &rarr; imports the `hmac` module for its `compare_digest()` function
- **line 13** &rarr; hashes the password being checked, using the **same** salt as the stored hash
- **line 14** &rarr; `hmac.compare_digest()` checks if the two hashes match. It takes the same amount of time whether the hashes match or not, so an attacker can't learn anything from how long the check takes. This is safer than using `==`
- **lines 17&ndash;18** &rarr; creates a salt and a stored hash, as if a user had just signed up
- **lines 20&ndash;21** &rarr; checks the correct password, then the same password with a capital C
:::

Output:

:::{code} text
True
False
:::

## Storing passwords in SQLite

Now let's put it all together in a login system. We'll store each user's username, salt and password hash in a SQLite database. Just like our other database code, the database code goes in a **Datastore** class.

Create a new file, add the code below and save it as ***datastore.py***.

:::{code} python
:linenos:
import hashlib
import hmac
import secrets
import sqlite3

ITERATIONS = 600_000


class Datastore:
    def __init__(self, db_file: str) -> None:
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                salt TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def hash_password(self, password: str, salt: bytes) -> bytes:
        return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)

    def add_user(self, username: str, password: str) -> None:
        salt = secrets.token_bytes(16)
        password_hash = self.hash_password(password, salt)
        self.cursor.execute(
            """
            INSERT INTO users (username, salt, password_hash)
            VALUES (:username, :salt, :password_hash)
            """,
            {
                "username": username,
                "salt": salt.hex(),
                "password_hash": password_hash.hex(),
            },
        )
        self.connection.commit()

    def check_login(self, username: str, password: str) -> bool:
        self.cursor.execute(
            """
            SELECT salt, password_hash
            FROM users
            WHERE username = :username
            """,
            {"username": username},
        )
        result = self.cursor.fetchone()
        if result is None:
            return False

        salt = bytes.fromhex(result[0])
        stored_hash = bytes.fromhex(result[1])
        new_hash = self.hash_password(password, salt)
        return hmac.compare_digest(new_hash, stored_hash)
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 11&ndash;12** &rarr; connects to the database file and creates a cursor
- **lines 13&ndash;22** &rarr; creates the `users` table if it doesn't already exist. `username` is the primary key, so no two users can have the same username
- **lines 24&ndash;25** &rarr; the same `hash_password()` function as before, now as a method
- **line 28** &rarr; creates a new random salt for the new user
- **line 29** &rarr; hashes the user's password with that salt
- **lines 30&ndash;41** &rarr; inserts the user using named placeholders. The salt and hash are bytes, so `.hex()` turns them into text to store in the `TEXT` columns
- **lines 44&ndash;51** &rarr; finds the salt and hash for the username
- **line 52** &rarr; `fetchone()` returns the first matching row, or `None` if there is no user with that username
- **lines 53&ndash;54** &rarr; if the username doesn't exist, the login fails
- **lines 56&ndash;57** &rarr; `bytes.fromhex()` turns the stored text back into bytes
- **lines 58&ndash;59** &rarr; hashes the password that was entered with the stored salt and compares the two hashes
:::

Now create ***main.py*** to use the Datastore:

:::{code} python
:linenos:
from datastore import Datastore

db = Datastore("data/users.db")

db.add_user("alex", "password123")

print(db.check_login("alex", "password123"))
print(db.check_login("alex", "Password123"))
print(db.check_login("jordan", "password123"))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports the `Datastore` class from ***datastore.py***
- **line 3** &rarr; connects to **users.db** in our **data** folder. SQLite creates the file if it doesn't exist
- **line 5** &rarr; adds a user called `alex`
- **line 7** &rarr; checks the correct password
- **line 8** &rarr; checks a password with a capital P
- **line 9** &rarr; checks a username that doesn't exist
:::

Output:

:::{code} text
True
False
False
:::

If we open **users.db** in DB Browser for SQLite, we can see that the password itself is never stored:

| username | salt | password_hash |
| --- | --- | --- |
| alex | 45762f5d44af3f51c28cfc86d4ab8ce5 | 64a4e1f8ae591eb7ff0960ad2bdbf0999cac32084e3abb3da653fc19c08ebb06 |

:::{caution} Running main.py twice
:class: dropdown
If we run ***main.py*** a second time, it crashes with this error:

```text
sqlite3.IntegrityError: UNIQUE constraint failed: users.username
```

`alex` is already in the database, and `username` is the primary key, so it can't be added again. Delete **users.db** or comment out line 5 before running it again. In a real app we would check that a username is free before adding the user.
:::

:::{hint} Login error messages
:class: dropdown
`check_login()` returns `False` for both a wrong password and a username that doesn't exist. Our app should show the same message for both, such as "Incorrect username or password". If it said "username not found", an attacker could use it to find out which usernames exist.
:::

## Summary

| Task | Code |
| --- | --- |
| Hash a string with SHA-256 | `hashlib.sha256(text.encode()).hexdigest()` |
| Make a random salt | `secrets.token_bytes(16)` |
| Hash a password | `hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)` |
| Compare two hashes safely | `hmac.compare_digest(hash1, hash2)` |
| Bytes to hexadecimal text | `data.hex()` |
| Hexadecimal text to bytes | `bytes.fromhex(text)` |

:::{seealso} Hashing Activities
:class: dropdown
**Activity 1: The avalanche effect**

Write a program that prints the SHA-256 hash of `"apple"`, `"Apple"` and `"apple "` (with a space at the end). How similar are the hashes?

Expected Output:

```text
'apple': 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
'Apple': f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd
'apple ': e0f6f390c37556b5eb3292a63159aea8ec795a4a1d4f22a18abb14ac7341508f
```

---

**Activity 2: Crack an unsalted hash**

An attacker has stolen this unsalted SHA-256 password hash:

```text
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```

Write a program that hashes each password in this list and checks if it matches the stolen hash:

```python
common_passwords = ["dragon", "sunshine", "monkey", "password", "football"]
```

Expected Output:

```text
Password found: password
```

Why does this attack show that passwords need to be salted and slow to hash?

---

**Activity 3: Same password, different hashes**

Write a function `hash_new_password(password: str) -> tuple[bytes, bytes]` that creates a random salt, hashes the password with `pbkdf2_hmac`, and returns the salt and the hash.

Call it three times with the password `"letmein"` and print each salt and the first 16 characters of each hash.

Expected Output (our salts and hashes will be different, but all three should be different from each other):

```text
salt: ba035f9b472ccf3a3fbd5620181de1f0  hash: 318338c9999a9440...
salt: 1eeee39121d3b690b0bb8964a5e532e8  hash: 0c78d650bb74f84e...
salt: 6973155159bd0d5ff200ee4593e7b17c  hash: 5c2aacd239976196...
```

---

**Activity 4: Change a password**

Add a `change_password(username, old_password, new_password)` method to the `Datastore` class. It should:

1. return `False` if the old password is wrong
2. otherwise, create a new salt, hash the new password, update the user's row with an `UPDATE` statement and return `True`

Test it with this ***main.py*** (after `alex` has been added with the password `password123`):

```python
from datastore import Datastore

db = Datastore("data/users.db")

print(db.change_password("alex", "wrong-password", "N3w-Passw0rd!"))
print(db.change_password("alex", "password123", "N3w-Passw0rd!"))
print(db.check_login("alex", "password123"))
print(db.check_login("alex", "N3w-Passw0rd!"))
```

Expected Output:

```text
False
True
False
True
```
:::
