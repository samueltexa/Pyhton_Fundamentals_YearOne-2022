import socket

def client_program():
    host = '192.168.43.31'
    port = 50000

    client_socket = socket.socket()
    client_socket.connect((host, port))  # Connect to the server

    device_name = client_socket.recv(1024).decode()  # Receive the device name from the server
    print(f"Connected to server, the server's device name is: {device_name}")

    client_socket.close()  # Close the client socket

if __name__ == '__main__':
    client_program()
