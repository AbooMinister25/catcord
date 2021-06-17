import time
import hashlib

token_count = 0


def gensnowflake():
    global token_count
    flake = time.time_ns().to_bytes(56, byteorder="big")
    flake += token_count.to_bytes(8, byteorder="big")
    token_count += 1
    if token_count == 256:
        token_count = 0
    return int.from_bytes(flake, byteorder="big")


def gentokenhash(token):
    tokenhash = hashlib.sha256(bytes(token, encoding="utf8")).hexdigest()
    return tokenhash
