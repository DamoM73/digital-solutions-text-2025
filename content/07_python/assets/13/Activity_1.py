import hashlib


def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


for word in ["apple", "Apple", "apple "]:
    print(f"{word!r}: {sha256_hash(word)}")
