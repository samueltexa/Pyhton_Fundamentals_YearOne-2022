import socket
import tkinter as mygui
from threading import Thread

server_window = mygui.Tk()
server_window.title("Server_Side")
server_window.geometry("500x350")
recievedMessagelbl = mygui.Label(server_window, text="Received messages:")
recievedMessagelbl.grid(row=0,column=0)
text_area = mygui.Text(server_window, state=mygui.DISABLED, height=10, width=60)
text_area.grid(row=1, column=0)
enterMessagelbl = mygui.Label(server_window , text="Enter your message Here:")
enterMessagelbl.grid(row=2,column=0)
text_field = mygui.Entry(server_window)
text_field.grid()


def receive_messages(conn, text_area):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        text_area.config(state=mygui.NORMAL)
        text_area.insert(mygui.END, data + '\n')
        text_area.config(state=mygui.DISABLED)

def server_program():
    def send_message():
        message = text_field.get()
        text_field.delete(0, mygui.END)
        conn.send(message.encode())

    def close_connection():
        conn.close()
        server_socket.close()
        server_window.quit()
        print("\nConnection from " + str(address) + " terminated successfully.")

    host = '0.0.0.0'
    port = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    server_socket.settimeout(10)

    try:
        conn, address = server_socket.accept()
        print("\nConnection from " + str(address) + " accepted successfully.")

        send_button = mygui.Button(server_window, text="Send", command=send_message, bg="green")
        send_button.grid()
        close_button = mygui.Button(server_window, text="Close", command=close_connection, bg="red")
        close_button.grid()
             
        receive_thread = Thread(target=receive_messages, args=(conn, text_area))
        receive_thread.daemon = True
        receive_thread.start()

        server_window.mainloop()
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        server_socket.close()
        

server_program()
