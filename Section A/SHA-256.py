import hashlib


def hash_password(password):
    # hashing using SHA-254
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

password = "password123"
hashed_password = hash_password(password)
print("Hashed Password", hashed_password)