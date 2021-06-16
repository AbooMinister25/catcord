import time
import hashlib
import random

def gensnowflake():
    flake = time.time_ns().to_bytes(56, byteorder='big')
    flake += random.randint(1, 900000).to_bytes(8, byteorder='big')
    return int.from_bytes(flake, byteorder='big')

def gentokenhash(token):
    tokenhash = hashlib.sha256(bytes(token, encoding='utf8')).hexdigest()
    return tokenhash
