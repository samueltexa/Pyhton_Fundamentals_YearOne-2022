import socket
import platform

def server_program():
    host = '0.0.0.0'
    port = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))

        server_socket.listen(5)  # Listen for incoming connections
        print("Server started, waiting for connections.")
        
        while True:
            conn, address = server_socket.accept()  # Accept a new client connection
            print(f"Connection from {address} established.")

            device_name = platform.node()  # Get the device/computer name
            conn.send(device_name.encode())  # Send the device name to the client

            conn.close()  # Close the client connection

    except OSError:
        print("Server already in use. Please wait for a moment.")
    finally:
        server_socket.close()  # Close the server socket

if __name__ == '__main__':
    server_program()
