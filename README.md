# Simple Chat Application

This is a basic client-server chat application developed in Python using the `socket` and `threading` modules. The application allows two clients to connect to a server and exchange messages in real-time.

## Features

- Real-time messaging between two clients
- Simple and easy-to-understand code
- Basic error handling to close connections gracefully

## Files

- `server.py`: This file contains the server-side code that handles client connections and message broadcasting.
- `client.py`: This file contains the client-side code for the first client.
- `client2.py`: This file contains the client-side code for the second client.

## Requirements

- Python 3.x

## How to Run

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the server**:
    ```bash
    python server.py
    ```

3. **Run the first client**:
    ```bash
    python client.py
    ```

4. **Run the second client**:
    ```bash
    python client2.py
    ```

## How It Works

1. The server starts and waits for two clients to connect.
2. Once both clients are connected, they can send messages to each other.
3. Each message sent by a client is broadcasted to the other client by the server.

## Code Explanation

### `server.py`
The server code listens for client connections and starts a new thread to handle each client. It broadcasts received messages to all connected clients except the sender.

```python
import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                client_socket.close()
                clients.remove(client_socket)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(2)
print("Server started and waiting for 2 clients to connect...")

while len(clients) < 2:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()

print("2 clients connected. They can now chat.")
