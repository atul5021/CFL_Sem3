import socket

def ed(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

key = b'KEY'  # The same key used by the client

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(1)
print("Server is listening on port 8080...")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr} established.")
    encrypted_data = conn.recv(1024)
    decrypted_data = ed(encrypted_data, key)
    print(f"Decrypted data: {decrypted_data.decode('utf-8')}") 
    conn.close()
