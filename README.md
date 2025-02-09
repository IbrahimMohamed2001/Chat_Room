# Chat Application

This is a simple chat application built using Python's `socket` and `threading` modules. It consists of a server and a client that can communicate with each other over a network.

## Files

- `server.py`: The server script that handles multiple clients and broadcasts messages to all connected clients.
- `client.py`: The client script that connects to the server and allows the user to send and receive messages.

## How to Run

### Server

1. Open a terminal.
2. Navigate to the directory containing `server.py`.
3. Run the server script:
    ```sh
    python server.py
    ```

### Client

1. Open a terminal.
2. Navigate to the directory containing .
3. Run the client script:
    ```sh
    python client.py
    ```
4. Enter an alias when prompted.
5. Start sending and receiving messages.

## Features

- Multiple clients can connect to the server.
- Clients can send and receive messages in real-time.
- The server broadcasts messages to all connected clients.
- Clients are notified when a new client joins or leaves the chat room.