import hashlib
import time

token_count = 0


def generate_sha256(string: str) -> str:
    hashed = hashlib.sha256(bytes(string, encoding="utf-8")).hexdigest()
    hashed = hashlib.sha256(bytes(hashed, encoding="utf-8")).hexdigest()
    return hashed


def gensnowflake() -> int:
    global token_count
    flake = time.time_ns().to_bytes(56, byteorder="big")
    flake += token_count.to_bytes(8, byteorder="big")
    token_count += 1
    token_count %= 256
    return int.from_bytes(flake, byteorder="big")
