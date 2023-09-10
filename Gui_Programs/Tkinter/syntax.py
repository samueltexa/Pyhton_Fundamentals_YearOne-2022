import tkinter as tk
window  = tk.Tk()

#setting title
window.title("MY FIRST GUI IN PYTHON")

# Change the background color
window.configure(bg="grey")  # Set the background color to blue


#Methods of setting the window size

# 1. CONFIGURE METHOD===>Alternatively, use the configure method to set the window size
#window.configure(width=400, height=300)

"""GEOMETRY
    window.geometry("500"x"500")
"""

"""
MAKING THE WINDOW FIT THE SIZE OF THE SCREEN
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")"""

# Mking the window appear in the center of the scree.===>Get the screen width and height
window_width = 650
window_height = 600
# window.configure(width=650, height=600)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered

x = (screen_width - window_width) //2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


#adding components to the window
name = tk.Label(window, text = "Name")
name.grid(row = 0, column=0)
txtfield1 = tk.Entry(window)
txtfield1.grid(row = 0, column=1)

regno = tk.Label(window, text = "RegNo")
regno.grid(row = 2, column=0, padx=10, pady=10)
txtfield2 = tk.Entry(window)
txtfield2.grid(row = 2, column=1, padx=10, pady=10)

save = tk.Button(window, text = "Save")
save.grid(row= 4, column= 1)



window.mainloop() #main event loop
#Alternative
"""while True:
mywindow.update()"""