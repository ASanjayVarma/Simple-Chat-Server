import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"\nFriend: {message}\nYou: ", end="")
        except:
            print("\nConnection closed by the server.")
            client_socket.close()
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

threading.Thread(target=receive_messages, args=(client,)).start()

while True:
    message = input("You: ")
    client.send(message.encode('utf-8'))
