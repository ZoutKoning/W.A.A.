# Written by Zoie Rast
# 18 November, 2022
# Interface GUI

#Import the proper libraries
import tkinter as tk   
from tkinter import *
import datetime
import json

#Create and Initialize Window
window = tk.Tk()                #Create Window
window.geometry("400x400")      #Width and height of window
window.resizable(0,0)           #Makes window size fixed
window.title("Weather App")     #Window Title

greeting = tk.Label(text = "Welcome to Weather Activity App!") 
greeting.pack()         

# Display and push the label/entry to the popup
zip_value = StringVar()
zip_head= Label(window, text = 'Enter Zipcode:', font = 'Arial 12 bold').pack(pady = 10)  
inp_zip = Entry(window, textvariable = zip_value,  width = 24, font = 'Arial 14 bold').pack() #entry field

# This retrieves the zipcode after being entered
zipcode = inp_zip.get()

#Button to check the weather
Button(
    window, 
    command = weathercommand, 
    text = "Check the Weather", 
    font = "Arial 10", 
    bg = 'lightblue', 
    fg = 'black', 
    activebackground = "teal", 
    padx = 5, 
    pady = 5 
    ).pack(pady= 20)

#Weather Output
weather_now = Label(window, text = "Weather In Your Zipcode:", font = 'arial 12 bold').pack(pady = 10)

Button(
    window, 
    command = activitiescommand, 
    text = "Check Activities Avaliable", 
    font = "Arial 10", 
    bg = 'lightblue', 
    fg = 'black', 
    activebackground = "teal", 
    padx = 5, 
    pady = 5 
    ).pack(pady= 20)

#Activities Output
activities_now = Label(window, text = "Suggested Activities:", font = 'arial 12 bold').pack(pady = 10)

tfield = Text(window, width = 46, height = 10)
tfield.pack()
 
# This runs the loop for the window.
# This MUST remain at the end of the file!
window.mainloop()

