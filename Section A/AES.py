from Crypto.Cipher import AES

# Encrypt a message
message = "Hello, world!"

key = b"1234567890abcdef"
iv = b"0123456789abcdef"

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted_message = cipher.encrypt(message.encode())

print(encrypted_message)
