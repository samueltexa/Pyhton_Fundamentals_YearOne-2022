import socket
from threading import Thread

clients = []  # List to store connected clients

def receive_messages(conn, address):
    while True:
        try:
            message = conn.recv(1024).decode()  # Receive message from client
            if not message:
                break
            print("Received message from client", address, ":", message)
            broadcast_message(message, conn)  # Broadcast the message to all other clients
        except ConnectionResetError:
            break

    disconnect_client(conn)  # Disconnect the client

def disconnect_client(conn):
    for client in clients:
        if client[0] == conn:
            address = client[1]
            clients.remove(client)  # Remove the client from the list
            print(f"\nClient {address} disconnected from server")
            break

def broadcast_message(message, sender_conn):
    for client in clients:
        conn, _ = client
        if conn != sender_conn:
            try:
                conn.send(message.encode())  # Send the message to each connected client
            except BrokenPipeError:
                continue

def client_thread(conn, address):
    print("\nConnection from", address, "established successfully.")
    clients.append((conn, address))  # Add the client to the list of connected clients

    receive_thread = Thread(target=receive_messages, args=(conn, address))
    receive_thread.daemon = True
    receive_thread.start()

def server_program():
    host = '0.0.0.0'
    port = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for incoming connections
    print("\nServer started, waiting for connections.")
    server_socket.settimeout(20)  # Set a timeout for accepting connections

    try:
        while True:
            try:
                conn, address = server_socket.accept()  # Accept a new client connection
                client_thread(conn, address)  # Start a new thread to handle the client
            except socket.timeout:
                continue
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        for client in clients:
            client[0].close()  # Close all client connections
        server_socket.close()  # Close the server socket

if __name__ == '__main__':
    server_program()
