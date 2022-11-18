# Written by Zoie Rast
# 18 November, 2022
# Interface GUI

import tkinter as tk    # Import tkinter for the GUI
window = tk.Tk()        # Create a window

greeting = tk.Label(text = "Welcome to Weather Activity App!") # Greeting in popup
greeting.pack()         # This puts the greeting into the popup

labelzip = tk.Label(text = "Enter your zipcode:")
entryzip = tk.Entry()

# Display and push the label/entry to the popup
labelzip.pack()
entryzip.pack()

# This retrieves the zipcode after being entered
zipcode = entryzip.get()

# THIS IS A WIP FOR BUTTONS!!!!
button = tk.Button(
    text = "Click here to see the weather near you!",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "yellow",
)

# This runs the loop for the window.
# This MUST remain at the end of the file!
window.mainloop()

