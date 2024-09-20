
import socket
import random

def encrypt_message(message):
    em = ""
    keys = []  # Initialize the keys list
    for i in message:
        key = random.randint(1, 50)
        keys.append(key)  # Fixed typo here
        em += chr(ord(i) + key)  # Use 'i' instead of 'char'
    return em, keys

def client():

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cs - client_socket
    cs.connect(('localhost', 6017))

    message = input("Enter the message to send: ")

    em, keys = encrypt_message(message)  # Call the renamed function
    ks = ','.join(map(str, keys))

    cs.send(f"{em}|{ks}".encode())  # Fixed the usage of .encode()

    print(f"Sent Encrypted Message: {em}")
    print(f"Sent Keys: {keys}")

    cs.close()  # Fixed from cs.clone() to cs.close()

if __name__ == "__main__":
    client()
