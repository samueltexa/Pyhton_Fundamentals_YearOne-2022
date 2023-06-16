import socket
import tkinter as mygui
from threading import Thread

clientwindow = mygui.Tk()
clientwindow .title("Client_Side")
clientwindow.geometry("500x350")
recievedMessagelbl = mygui.Label(clientwindow , text="Received messages")
recievedMessagelbl.grid(row=0,column=0)
text_area = mygui.Text(clientwindow , state=mygui.DISABLED, height=10, width=60)
text_area.grid(row=1, column=0)
enterMessagelbl = mygui.Label(clientwindow , text="Enter your message Here:")
enterMessagelbl.grid(row=2,column=0)
text_field = mygui.Entry(clientwindow )
text_field.grid()

def receive_messages(client_socket, text_area):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        text_area.config(state=mygui.NORMAL)
        text_area.insert(mygui.END, message + '\n')
        text_area.config(state=mygui.DISABLED)

def client_program():
    def send_message():
        message = text_field.get()
        text_field.delete(0, mygui.END)
        client_socket.send(message.encode())

    def close_connection():
        client_socket.close()
        clientwindow .quit()
        print("\nConnection closed on address " + str(host) + " and port " +str(port)+ " successfully.")

    host = 'localhost'
    port = 50000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("\nConnection established on address " + str(host) + " and port " +str(port)+ " successfully.")
    
    send_button = mygui.Button(clientwindow , text="Send", command=send_message, bg="green")
    send_button.grid()
    close_button = mygui.Button(clientwindow , text="Close", command=close_connection, bg="red")
    close_button.grid()

    receive_thread = Thread(target=receive_messages, args=(client_socket, text_area))
    receive_thread.daemon = True
    receive_thread.start()

    clientwindow.mainloop()
    client_socket.close()

client_program()