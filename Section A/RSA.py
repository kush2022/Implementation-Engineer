from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)

public_key = key.publickey().exportKey()
private_key = key.exportKey()

# Encrypt a message
message = "Hello, world!"

encrypted_message = RSA.encrypt(message.encode(), public_key)

print(encrypted_message)
