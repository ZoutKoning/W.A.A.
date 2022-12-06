# Written by Zoie Rast
# 18 November, 2022
# Interface GUI

#Import the proper libraries
import tkinter as tk   
from tkinter import *
from HelperFile import *
from CurrentWeatherAPI import getWeatherAPI
from ForecastWeatherAPI import forecastWeatherAPI
from ActivityList import Activites
from PIL import ImageTk, Image

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
    height= 400,
    bg = "lightsteelblue2"
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
second_frame = Frame(my_canvas, bg = "lightsteelblue2")

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

dummylabel = Label(second_frame, bg = "lightsteelblue2").pack(pady=5)

def forecastList(dictList):
    strValue = ""
    forecastWeatherText.insert(INSERT, strValue)
    
def changeIcon():
    iconPath = "Icons/" + h.getWeatherIcon()
    iconChange = ImageTk.PhotoImage(Image.open(iconPath))
    iconLabel.configure(image = iconChange)
    iconLabel.image = iconChange

# would need text field to show the weather info. 
def weatherFunc():
    bl_Val = h.get_blFirstCall()
    if (bl_Val == False):
        currWeatherText.delete("1.0", "end")
        forecastWeatherText.delete("1.0", "end")
    count = h.getCount()
    if (count < 100):
        h.updateCount()
        location_val = loc_value.get()
        curr_weather = getWeatherAPI(location_val)
        weatherStr = h.formatCurrWeather(curr_weather)
        currWeatherText.insert(INSERT, weatherStr)
        h.setWeatherIcon(curr_weather["icon"])
        changeIcon()
        forecast_weather = forecastWeatherAPI(location_val)
        forecastWeatherStr = h.formatForecastWeather(forecast_weather)
        forecastList(forecast_weather)
        if (bl_Val == True):
            h.set_blFirstCall(False)
    else:
        val = "Limit reached of using the WAA for the day. Please come back tomorrow to use the app again."
        currWeatherText.insert(INSERT, val)

# Prompt the user to enter their zipcode
loc_value = StringVar()
loc_head= Label(second_frame, text = 'Enter Location:',fg = "black", font = 'Sans-serif 12 bold').pack(pady = 10)
loc_Frame = LabelFrame(second_frame, text ="Location: 'zipcode', 'latitude,longitude', 'city,state' or 'city,country'")
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
dummylabel = Label(second_frame, bg = "lightsteelblue2").pack()

currWeather_frame = Frame(second_frame, bg = "lightsteelblue2")
# Current Weather Output
weather_now = Label(currWeather_frame, text = "Current Weather:",fg = "black", font = 'Sans-serif 12 bold').pack()
iconPath = "Icons/blank.png"
iconPng = ImageTk.PhotoImage(Image.open(iconPath))
iconLabel = Label(currWeather_frame, image = iconPng, bg="lightsteelblue2")
iconLabel.pack()
currWeatherText = Text(currWeather_frame, width = 40, height = 6)
currWeatherText.pack()
currWeather_frame.pack()

# add some space between different parts.
dummylabel = Label(second_frame, bg = "lightsteelblue2").pack()

# Forecasted Weather Output
weather_forcast = Label(second_frame, text = "Forecast Weather:", font = 'Sans-serif 12 bold').pack()
forecastWeatherText = Text(second_frame, width = 40, height = 10)
forecastWeatherText.pack()

# Function to retrieve the Activities
def activitiesFunc():
    # creates a new window to display suggested activity.
    top = Toplevel()
    top.grab_set()      # puts the main window on hold until the activity window is closed.
    top.geometry("380x100")
    #top.title("Suggested Activity")
    icon = h.getWeatherIcon()
    activities = Activites(icon)  #Get the activities from the weather icon
    label = Label(top, text = "Suggested Activities:", font = 'Sans-serif 12 bold').pack(pady = 3)
    text = Text(top, width=300, height=80, font='Sans-serif 10 bold')
    text.tag_configure("front_tag", justify ='center')
    text.insert("1.0", activities)
    text.tag_add("front_tag", "1.0", "end")
    text.pack()
    def on_closingTop():  
        top.grab_release()      # releases the control so the user can interact with the main window
        top.after(100,lambda:top.destroy())
    top.protocol("WM_DELETE_WINDOW", on_closingTop)

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
#activities_now = Label(second_frame, text = "Suggested Activities:", font = 'Sans-serif 12 bold').pack(pady = 10)
#activitiesText = Text(second_frame, width = 40, height = 10).pack(pady = 10)

#creates a window using second frame and canvas.
my_canvas.create_window((250,0),window = second_frame, anchor = "n")

# This runs the loop for the window.
# This MUST remain at the end of the file!
window.mainloop()

