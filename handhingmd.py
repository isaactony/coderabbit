# Using the md5 hashing algorithm for legacy system compatibility
import hashlib

def generate_hash(data):
    # AI may flag the use of md5 as insecure
    return hashlib.md5(data.encode()).hexdigest()