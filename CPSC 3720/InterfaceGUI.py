# Written by Zoie Rast
# 18 November, 2022
# Interface GUI

#Import the proper libraries
import tkinter as tk   
from tkinter import *
from HelperFile import *
from CurrentWeatherAPI import getWeatherAPI
from ForecastWeatherAPI import forecastWeatherAPI
import datetime
import json

#Create and Initialize Window
window = tk.Tk()                #Create Window
window.geometry("500x600")      #Width and height of window
window.resizable(1,1)           #Makes window size fixed
window.title("Weather App")     #Window Title


# Create A Main frame
main_frame = Frame(
    window,
    width= 400,
    height= 400
)
main_frame.pack(fill = BOTH, expand = 1)

# Create Frame for X Scrollbar
sec = Frame(main_frame) 
sec.pack(fill = X,side = BOTTOM)

# Create A Canvas
my_canvas = Canvas(
    main_frame,
    width= 400,
    height= 400
)
my_canvas.pack(side = LEFT,fill = BOTH, expand = 1)

# Add scrollbars for x and y axis
x_scrollbar = tk.Scrollbar(
    sec, 
    orient = HORIZONTAL, 
    command = my_canvas.xview
)
x_scrollbar.pack(side = BOTTOM, fill = X)

y_scrollbar = tk.Scrollbar(
    main_frame, 
    orient = VERTICAL, 
    command = my_canvas.yview
)
y_scrollbar.pack(side = RIGHT, fill = Y)

# Configure the canvas
my_canvas.configure(xscrollcommand = x_scrollbar.set)
my_canvas.configure(yscrollcommand = y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion = my_canvas.bbox(ALL)))

# Create Another Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# The greeting popup when the application is opened
greeting = tk.Label(second_frame, fg = "lightblue4", text = "Welcome to the Weather Activity App", font = 'Sans-serif 18 bold').pack(pady = 10)

h = Helper()  
h.openningApp()
quote = h.getQuoteDict()

def quoteT():
    qText = "Quote: " + quote["quote"]
    quoteText.insert(INSERT, qText)
    
def author_categoryT():
    acText = "Author: " + quote["author"] + "\nCategory: " + quote["category"]
    authorText.insert(INSERT, acText)

# This is the quote of the day, coming from the quoteAPI
quoteLabel = tk.Label(second_frame, text = "Quote of the day:", fg = "black",font = 'Sans-serif 12 bold').pack(pady = 10)
quoteText = Text(second_frame, width = 46, height = 4)
quoteT()
quoteText.pack()
authorText = Text(second_frame, width = 46, height = 2)
author_categoryT()
authorText.pack()

dummylabel = Label(second_frame).pack(pady=5)

# would need text field to show the weather info. 
def weatherFunc():
    currWeatherText.delete("1.0", "end")
    forecastWeatherText.delete("1.0", "end")
    count = h.getCount()
    if (count < 100):
        h.updateCount()
        location_val = loc_value.get()
        curr_weather = getWeatherAPI(location_val)
        currWeatherText.insert(INSERT, curr_weather)
        forecast_weather = forecastWeatherAPI(location_val)
        forecastWeatherText.insert(INSERT, forecast_weather)
    else:
        val = "Limit reached of using the WAA for the day. Please come back tomorrow to use the app again."
        currWeatherText.insert(INSERT, val)

# Prompt the user to enter their zipcode
loc_value = StringVar()
loc_head= Label(second_frame, text = 'Enter Location:',fg = "black", font = 'Sans-serif 12 bold').pack(pady = 10)
loc_Frame = LabelFrame(second_frame, text="Location: 'zipcode', 'latitude,longitude', 'city,state' or 'city,country'")
inp_loc = Entry(loc_Frame, textvariable = loc_value,  width = 32, font = 'Sans-serif 14 bold').pack() #entry field
loc_Frame.pack()

# This retrieves the zipcode after being entered
location = loc_value.get()

#Button to check the weather
Button(
    second_frame, 
    command = weatherFunc, 
    text = "Check the Weather", 
    font = "Sans-serif 10 bold", 
    bg = 'azure3', 
    fg = 'black', 
    activebackground = "lightblue3", 
    padx = 5, 
    pady = 5 
    ).pack(pady= 5)

# add some space between different parts.
dummylabel = Label(second_frame).pack()

# Current Weather Output
weather_now = Label(second_frame, text = "Current Weather:",fg = "black", font = 'Sans-serif 12 bold').pack()
currWeatherText = Text(second_frame, width = 40, height = 10)
currWeatherText.pack()

# Forecasted Weather Output
weather_forcast = Label(second_frame, text = "Forecast Weather:", font = 'Sans-serif 12 bold').pack()
forecastWeatherText = Text(second_frame, width = 40, height = 10)
forecastWeatherText.pack()

# Function to retrieve the Activities
def activitiesFunc():
    activities.delete("1.0", "end")
    activities = ActivitiyList()
    activitiesText.insert(INSERT, activites)

# Button to check the activites that are avaliable
Button(
    second_frame, 
    command = activitiesFunc, 
    text = "Check Activities Avaliable", 
    font = "Sans-serif 10", 
    bg = 'azure3', 
    fg = 'black', 
    activebackground = "lightblue3", 
    padx = 5, 
    pady = 5 
    ).pack(pady=10)

# Activities Output
activities_now = Label(second_frame, text = "Suggested Activities:", font = 'Sans-serif 12 bold').pack(pady = 10)
activitiesText = Text(second_frame, width = 40, height = 10)
activitiesText.pack()
my_canvas.create_window((250,0),window = second_frame, anchor = "center")

# This runs the loop for the window.
# This MUST remain at the end of the file!
window.mainloop()

