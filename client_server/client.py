import socket

def client_program():
    host = '192.168.43.31'
    port = 50000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    device_name = client_socket.recv(1024).decode()
    print(f"Connected to server, the server's device name is: {device_name}")

    client_socket.close()

if __name__ == '__main__':
    client_program()
