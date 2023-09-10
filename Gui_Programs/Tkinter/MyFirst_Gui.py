import tkinter as   mygui
mywindow = mygui.Tk()
mywindow.title("MY FIRST GUI")
# Window sizes
window_width = 650
window_height = 600

#Screen size
screen_width = mywindow.winfo_screenwidth()
screen_height = mywindow.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - window_width)//2
y = (screen_height - window_height)//2
mywindow.geometry(f"{window_width}x{window_height}+{x}+{y}") 

label = mygui.Label(mywindow, text="Name")
label.pack()
# Adding a button
button = mygui.Button(mywindow, text="Save!")
button.pack()  # To add the button to the window
textfield = mygui.Entry(mywindow)
textfield.pack()
mywindow.mainloop()