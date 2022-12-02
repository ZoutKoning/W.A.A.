import tkinter as tk   
from tkinter import *
import datetime
import json
from HelperFile import *
from CurrentWeatherAPI import *


# Initilize the Tkinter Window

root = Tk()
root.geometry("600x600")  # size of the window
root.resizable(1,1)  # to make window size fixed

# title of the window
root.title("Weather Activity App (WAA)")

# frame
frame = Frame(
    root,
    width= 400,
    height= 400,
    bg= "sky blue"
)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(
    frame,
    bg= "white",
    width= 400,
    height= 400,
    scrollregion= (0,0,500,600)
)

verticalBar = Scrollbar(
    frame, 
    orient=VERTICAL
)
verticalBar.pack(side=RIGHT, fill=Y)
verticalBar.config(command=canvas.yview)

horizontalBar = Scrollbar(
    frame,
    orient=HORIZONTAL
)
horizontalBar.pack(side=BOTTOM,fill=X)
horizontalBar.config(command=canvas.xview)

canvas.config(width=400, height=400)

canvas.config(
    xscrollcommand=horizontalBar.set,
    yscrollcommand=verticalBar.set 
)
canvas.pack(expand=True, side=LEFT, fill=BOTH)

second_frame = Frame(canvas, width = 400, height = 400, background="sky blue")
# Welcome greeting to the users when they open the app.
greeting = LabelFrame(second_frame)
greetingLabel = Label(greeting, text="Welcome to Weather Activity App!")
greetingLabel.config(font = 'Sans-serif 10 bold')
greetingLabel.pack(padx=2, pady=2)
greeting.pack(padx=10, pady=10)

h = Helper()  
h.openningApp()
quote = h.getQuoteDict()

def quoteT():
    qText = "Quote: " + quote["quote"]
    qotd_Q.insert(INSERT, qText)
    
def author_categoryT():
    acText = "Author: " + quote["author"] + "\nCategory: " + quote["category"]
    qotd_AC.insert(INSERT, acText)


qotd_Frame = LabelFrame(second_frame, text="Quote of the day!")
qotd_Q = Text(qotd_Frame, height=5, width=60, wrap=WORD)
quoteT()
qotd_Q.pack(padx = 2, pady = 2, expand=True, fill=BOTH)
qotd_AC = Text(qotd_Frame, height=2, width=20, wrap=WORD)
author_categoryT()
qotd_AC.pack(padx = 2, pady = 2, side=BOTTOM, expand=True, fill=X)
qotd_Frame.pack()

def weatherFunc():
    weatherText.delete("1.0", "end")
    count = h.getCount()
    if (count < 100):
        h.updateCount()
        location_val = loc_value.get()
        curr_weather = getWeatherAPI(location_val)
        weatherText.insert(INSERT, curr_weather)
    else:
        val = "Limit reached of using the WAA for the day. Please come back tomorrow to use the app again."
        weatherText.insert(INSERT, val)

loc_value = StringVar()
loc_Frame = LabelFrame(second_frame, text="Location: 'zipcode', 'latitude,longitude', 'city,state' or 'city,country'")
loc_Label = Label(loc_Frame, text= "Location:", width=10)
loc_Label.config(font = 'Sans-serif 10 bold')
loc_Label.pack(padx = 2, pady = 2, side = LEFT)
loc_entry = Entry(loc_Frame, textvariable= loc_value, width=40).pack(side=LEFT)
loc_button = Button(loc_Frame, command = weatherFunc, text="Check Weather", width=20)
loc_button.pack(padx = 2, pady = 2, side=LEFT)
loc_Frame.pack(padx = 10, pady = 10)

weather_Frame = LabelFrame(second_frame)
weatherText = Text(weather_Frame, width=60, height=4)
weatherText.pack(padx = 2, pady = 2)
weather_Frame.pack()

canvas.create_window((40, 0), window=second_frame, anchor="nw")
root.mainloop()