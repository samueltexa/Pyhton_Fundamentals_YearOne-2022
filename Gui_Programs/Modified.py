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

def on_entry_event(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, tk.END)
        entry_widget.config(foreground="black")

def on_leave_event(event, entry_widget, placeholder):
    if entry_widget.get() == "":
        entry_widget.insert(0, placeholder)
        entry_widget.config(foreground="gray")

window = tk.Tk()
window.title("MY FIRST GUI IN PYTHON")

window_width = 650
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

name = tk.Label(window, text="Name")
name.grid(row=0, column=0)
txtfield1 = tk.Entry(window, width=28, foreground="gray")
txtfield1.insert(0, "Enter your name here")
txtfield1.bind("<FocusIn>", lambda event: on_entry_event(event, txtfield1, "Enter your name here"))
txtfield1.bind("<FocusOut>", lambda event: on_leave_event(event, txtfield1, "Enter your name here"))
txtfield1.grid(row=0, column=1)

regno = tk.Label(window, text="RegNo")
regno.grid(row=2, column=0, padx=10, pady=10)
txtfield2 = tk.Entry(window, foreground="gray", width=28)
txtfield2.insert(0, "Enter registration number here")
txtfield2.bind("<FocusIn>", lambda event: on_entry_event(event, txtfield2, "Enter registration number here"))
txtfield2.bind("<FocusOut>", lambda event: on_leave_event(event, txtfield2, "Enter registration number here"))
txtfield2.grid(row=2, column=1, padx=10, pady=10)

save = tk.Button(window, text="Save", command=save_data)
save.grid(row=4, column=1)

window.mainloop()