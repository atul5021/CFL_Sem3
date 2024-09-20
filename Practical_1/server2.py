import socket

def dm(em, keys):   # dm - decrypt_message | em encrypted_message
    dm = ""
    for i in range(len(em)):
        dm += chr(ord(em[i]) - keys[i])
    return dm

def server():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ss - server_socket
    ss.bind(('localhost', 6017))

    ss.listen(1)
    print("Server is listening......")

    conn, ip = ss.accept()
    print(f"Connection from {ip}")

    data = conn.recv(1024).decode()  # Fix: receive the data and then decode it

    em, ks = data.split('|')  # ks - key_string
    keys = list(map(int, ks.split(',')))

    print(f"Received Encrypted message: {em}")
    print(f"Received Keys: {keys}")

    # Decrypt the message 
    dms = dm(em, keys)
    print(f"Decrypted Message: {dms}")

    conn.close()

if __name__ == "__main__":
    server()
