import hashlib
import time
from dataclasses import dataclass


@dataclass
class TokenCount:
    count: int = 0

    def increment(self):
        self.count += 1
        self.count %= 256


token_count = TokenCount()


def generate_sha256(string: str) -> str:
    hashed = hashlib.sha256(bytes(string, encoding="utf-8")).hexdigest()
    hashed = hashlib.sha256(bytes(hashed, encoding="utf-8")).hexdigest()
    return hashed


def gensnowflake() -> int:
    flake = time.time_ns().to_bytes(56, byteorder="big")
    flake += token_count.count.to_bytes(8, byteorder="big")
    token_count.increment()
    return int.from_bytes(flake, byteorder="big")
