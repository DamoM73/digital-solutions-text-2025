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

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        if not self.check_login(username, old_password):
            return False

        salt = secrets.token_bytes(16)
        password_hash = self.hash_password(new_password, salt)
        self.cursor.execute(
            """
            UPDATE users
            SET salt = :salt, password_hash = :password_hash
            WHERE username = :username
            """,
            {
                "username": username,
                "salt": salt.hex(),
                "password_hash": password_hash.hex(),
            },
        )
        self.connection.commit()
        return True


