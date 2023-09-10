import tkinter as tk
from tkinter import ttk

def start_drag(event):
    # Initiate the drag operation
    widget = event.widget
    widget.start_drag(event.x_root, event.y_root, widget.get_dragged_type())

def accept_drop(event):
    # Accept the dropped data
    widget = event.widget
    widget.accept_drop(tk.DND.DROP_COPY)

def end_drag(event):
    # End the drag operation
    widget = event.widget
    widget.end_drag()

def handle_drop(event):
    # Handle the dropped data
    widget = event.widget
    data = widget.get_drop_data()
    print(f"Dropped data: {data}")

root = tk.Tk()

# Create a label with drag and drop support
label = ttk.Label(root, text="Drag me!")

label.bind("<<DragInitCmd>>", start_drag)
label.bind("<<DragEnter>>", accept_drop)
label.bind("<<DragEndCmd>>", end_drag)
label.bind("<<Drop>>", handle_drop)
label.pack()

root.mainloop()
