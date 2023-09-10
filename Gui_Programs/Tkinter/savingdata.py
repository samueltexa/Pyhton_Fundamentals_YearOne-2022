import tkinter as tk
from tkinter import messagebox

def save_data():
    name = txtfield1.get()
    regno = txtfield2.get()

    with open("data.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"RegNo: {regno}\n")

    txtfield1.delete(0, tk.END)
    txtfield2.delete(0, tk.END)

    messagebox.showinfo("Success", "Data saved successfully!")

def on_entry_click(event):
    if txtfield2.get() == "Enter registration number here":
        txtfield2.delete(0, tk.END)
        txtfield2.config(foreground="black")

def on_entry_leave(event):
    if txtfield2.get() == "":
        txtfield2.insert(0, "Enter registration number here")
        txtfield2.config(foreground="gray")

def on_name_entry_click(event):
    if txtfield1.get() == "Enter your name here":
        txtfield1.delete(0, tk.END)
        txtfield1.config(foreground="black")

def on_name_entry_leave(event):
    if txtfield1.get() == "":
        txtfield1.insert(0, "Enter your name here")
        txtfield1.config(foreground="gray")
        
def header():
    lableh = tk.Label(window,text="Adiministration Log In", bg = "green")
    lableh.grid(row=0, column=1,padx=0,pady=5)

window = tk.Tk()
header()
window.title("MY FIRST GUI IN PYTHON")

window_width = 650
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


name = tk.Label(window, text="Name", bg="blue")
name.grid(row=1, column=0)
txtfield1 = tk.Entry(window, width=28, foreground="gray")
txtfield1.insert(1, "Enter your name here")
txtfield1.bind("<FocusIn>", on_name_entry_click)
txtfield1.bind("<FocusOut>", on_name_entry_leave)
txtfield1.grid(row=1, column=1)

regno = tk.Label(window, bg ="blue", text="RegNo")
regno.grid(row=2, column=0, padx=0, pady=10)
txtfield2 = tk.Entry(window, foreground="gray", width=28)
txtfield2.insert(0, "Enter registration number here")
txtfield2.bind("<FocusIn>", on_entry_click)
txtfield2.bind("<FocusOut>", on_entry_leave)
txtfield2.grid(row=2, column=1, padx=0, pady=10)

save = tk.Button(window, text="Save", bg = "green", command=save_data)
save.grid(row=4, column=1)

window.mainloop()
