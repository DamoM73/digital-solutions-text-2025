import hashlib
from pathlib import Path


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


Path("data/a.txt").write_bytes(b"Hello")
Path("data/b.txt").write_bytes(b"Hello")
Path("data/c.txt").write_bytes(b"hello")

files = [Path("data/a.txt"), Path("data/b.txt"), Path("data/c.txt")]

for i in range(len(files)):
    for j in range(i + 1, len(files)):
        if sha256_file(files[i]) == sha256_file(files[j]):
            print(f"{files[i].name} and {files[j].name} are identical")
        else:
            print(f"{files[i].name} and {files[j].name} are different")
