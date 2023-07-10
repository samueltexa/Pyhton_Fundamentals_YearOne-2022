import socket
import tkinter as mygui
from threading import Thread

clientwindow = mygui.Tk()
clientwindow.title("Client_Side")
clientwindow.geometry("500x350")

# Label for received messages
received_message_lbl = mygui.Label(clientwindow, text="Received messages")
received_message_lbl.grid(row=0, column=0)

# Text area to display received messages
text_area = mygui.Text(clientwindow, state=mygui.DISABLED, height=10, width=60)
text_area.grid(row=1, column=0)

# Label for entering a message
enter_message_lbl = mygui.Label(clientwindow, text="Enter your message here:")
enter_message_lbl.grid(row=2, column=0)

# Text field for entering a message
text_field = mygui.Entry(clientwindow)
text_field.grid()

def receive_messages(client_socket, text_area):
    while True:
        message = client_socket.recv(1024).decode()  # Receive message from server
        if not message:
            break
        text_area.config(state=mygui.NORMAL)
        text_area.insert(mygui.END, message + '\n')  # Display the received message
        text_area.config(state=mygui.DISABLED)

def send_message(client_socket):
    message = text_field.get()  # Get the message from the text field
    text_field.delete(0, mygui.END)  # Clear the text field
    client_socket.send(message.encode())  # Send the message to the server

def close_connection(client_socket):
    client_socket.close()  # Close the client socket
    clientwindow.quit()  # Quit the GUI window
    print("\nConnection closed successfully.")

def client_program():
    host = 'localhost'
    port = 50000

    client_socket = socket.socket()
    client_socket.connect((host, port))  # Connect to the server
    print("\nConnection established on address " + str(host) + " and port " + str(port) + " successfully.")

    # Send button to send messages
    send_button = mygui.Button(clientwindow, text="Send", command=lambda: send_message(client_socket), bg="green")
    send_button.grid()

    # Close button to close the connection
    close_button = mygui.Button(clientwindow, text="Close", command=lambda: close_connection(client_socket), bg="red")
    close_button.grid()

    # Start a thread to receive messages from the server
    receive_thread = Thread(target=receive_messages, args=(client_socket, text_area))
    receive_thread.daemon = True
    receive_thread.start()

    clientwindow.mainloop()  # Start the GUI event loop
if __name__ == '__main__':
    client_program()
