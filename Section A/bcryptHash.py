import bcrypt

def hash_password_bcrypt(password):
    # Hashing using bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

password = "securepassword123"
hashed_password = hash_password_bcrypt(password)
print("Hashed Password:", hashed_password)
