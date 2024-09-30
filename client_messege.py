import socket

def ed(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

key = b'KEY'  
key_values = [b for b in key]

# Set up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
data = input("Enter the text here: ").encode("utf-8")
encrypted_data = ed(data, key)
encrypted_values = list(encrypted_data)

# Print the key values and the encrypted message
print(f"Key values: {key_values}")
print(f"Encrypted message (as integers): {encrypted_values}")

# Send the encrypted data
client.send(encrypted_data)
client.close()
