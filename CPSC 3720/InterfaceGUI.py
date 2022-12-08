# Written by Zoie Rast and Vedant Patel
# 18 November, 2022
# Interface GUI

#Import the proper libraries
import tkinter as tk   
from tkinter import *
from HelperFile import *
from CurrentWeatherAPI import getWeatherAPI
from ForecastWeatherAPI import forecastWeatherAPI
from ForecastWindow import openWindow
from ActivityList import Activites
from PIL import ImageTk, Image
from pathlib import Path

#Create and Initialize Window
window = tk.Tk()                #Create Window
window.geometry("500x600")      #Width and height of window
window.resizable(True, True)           #Makes window size fixed
window.title("Weather App")     #Window Title


# Create A Main frame
main_frame = tk.Frame(
    window,
    width= 400,
    height= 400
)
main_frame.pack(fill = tk.BOTH, expand = 1)

# Create Frame for X Scrollbar
sec = tk.Frame(main_frame) 
sec.pack(fill = tk.X,side = tk.BOTTOM)

# Create A Canvas
my_canvas = tk.Canvas(
    main_frame,
    width= 400,
    height= 400,
    bg = "lightsteelblue2"
)
my_canvas.pack(side = tk.LEFT,fill = tk.BOTH, expand = 1)

# Add scrollbars for x and y axis
x_scrollbar = tk.Scrollbar(
    sec, 
    orient = tk.HORIZONTAL, 
    command = my_canvas.xview
)
x_scrollbar.pack(side = tk.BOTTOM, fill = tk.X)

y_scrollbar = tk.Scrollbar(
    main_frame, 
    orient = tk.VERTICAL, 
    command = my_canvas.yview
)
y_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# Configure the canvas
my_canvas.configure(xscrollcommand = x_scrollbar.set)
my_canvas.configure(yscrollcommand = y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion = my_canvas.bbox(tk.ALL)))

# Create Another Frame INSIDE the Canvas
second_frame = tk.Frame(my_canvas, bg = "lightsteelblue2")

# The greeting popup when the application is opened
greeting = tk.Label(second_frame, fg = "lightblue4", text = "Welcome to the Weather Activity App", font = 'Sans-serif 18 bold').pack(pady = 10)

# creates Helpers class object to call on the helper functions.
h = Helper()  
h.openningApp()
quote = h.getQuoteDict()

# used to update quote text in the app
def quoteT():
    qText = "Quote: " + quote["quote"]
    quoteText.insert(tk.INSERT, qText)
    quoteText.config(state=tk.DISABLED)
    
# used to update author and category info underneath the quote text. 
def author_categoryT():
    acText = "Author: " + quote["author"] + "\nCategory: " + quote["category"]
    authorText.insert(tk.INSERT, acText)
    authorText.config(state=tk.DISABLED)

# This is the quote of the day, coming from the quoteAPI
quoteLabel = tk.Label(second_frame, text = "Quote of the day:", fg = "black",font = 'Sans-serif 12 bold').pack(pady = 10)
quoteText = tk.Text(second_frame, width = 46, height = 4, wrap=tk.WORD)
quoteT()
quoteText.pack()
authorText = tk.Text(second_frame, width = 46, height = 2, wrap=tk.WORD)
author_categoryT()
authorText.pack()

# dummy label to create some space
dummylabel = tk.Label(second_frame, bg = "lightsteelblue2").pack(pady=5)

# called on to change the icon of the current weather icon
def changeIcon():
    iconPath = "Icons/" + h.getWeatherIcon()
    iconChange = ImageTk.PhotoImage(Image.open(iconPath))
    iconLabel.configure(image = iconChange, bg= "white")
    iconLabel.image = iconChange

# called on to check the location info and update the current weather information/fields.
def weatherFunc():
    bl_Val = h.get_blFirstCall()
    if (bl_Val == False):
        currWeatherText.config(state=tk.NORMAL)
        currWeatherText.delete("1.0", "end")
        currWeatherText.config(state=tk.DISABLED)
    count = h.getCount()
    if (count < 100):
        location_val = loc_value.get()
        h.updateCount()
        curr_weather = getWeatherAPI(location_val)
        #curr_weather = h.testCurr()
        strDict = json.dumps(curr_weather)
        listE = ["error", "exception", "exceeded", "Endpoint", "not found"]
        if any(i in strDict for i in listE):
            currWeatherText.config(state=tk.NORMAL)
            currWeatherText.insert(tk.INSERT, strDict)
            strText = "\nPlease enter valid location and try again"
            currWeatherText.insert(tk.INSERT, strText)
            currWeatherText.config(state=tk.DISABLED)
            forecastBtn.configure(state=tk.DISABLED)
            suggestActivityBtn.configure(state=tk.DISABLED)
            if (bl_Val == True):
                h.set_blFirstCall(False)
        else:
            weatherStr = h.formatCurrWeather(curr_weather)
            currWeatherText.config(state=tk.NORMAL)
            currWeatherText.insert(tk.INSERT, weatherStr)
            currWeatherText.config(state=tk.DISABLED)
            h.setWeatherIcon(curr_weather["icon"])
            changeIcon()
            forecastBtn.configure(state=tk.NORMAL)
            suggestActivityBtn.configure(state=tk.NORMAL)
            h.updateCount()
            forecast_weather = forecastWeatherAPI(location_val)
            h.setDictList(forecast_weather)
            if (bl_Val == True):
                h.set_blFirstCall(False)
    else:
        val = "Limit reached of using the WAA for the day. Please come back tomorrow to use the app again."
        currWeatherText.insert(tk.INSERT, val)
    

# Prompt the user to enter their location
loc_value = tk.StringVar()
loc_head= tk.Label(second_frame, text = 'Enter Location:',fg = "black", font = 'Sans-serif 12 bold').pack(pady = 10)
loc_Frame = tk.LabelFrame(second_frame, text ="Location: 'zipcode', 'latitude,longitude', 'city,state' or 'city,country'")
inp_loc = tk.Entry(loc_Frame, textvariable = loc_value,  width = 32, font = 'Sans-serif 14 bold').pack() #entry field
loc_Frame.pack()

# This retrieves the location after being entered
location = loc_value.get()

#Button to check the weather
tk.Button(
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
dummylabel = tk.Label(second_frame, bg = "lightsteelblue2").pack()

currWeather_frame = tk.Frame(second_frame, bg = "lightsteelblue2")
# Current Weather Output
weather_now = tk.Label(currWeather_frame, text = "Current Weather:",fg = "black", font = 'Sans-serif 12 bold').pack()
iconPath = "Icons/blank.png"
iconPng = ImageTk.PhotoImage(Image.open(iconPath))
iconLabel = tk.Label(currWeather_frame, image = iconPng, bg="lightsteelblue2")
iconLabel.pack()
currWeatherText = tk.Text(currWeather_frame, width = 40, height = 6, state=tk.DISABLED, wrap=tk.WORD)
currWeatherText.pack()
currWeather_frame.pack()

# add some space between different parts.
dummylabel = tk.Label(second_frame, bg = "lightsteelblue2").pack()

# called on when the user wants to see the forecast.
def callOpenWin():
    dictList = h.getDictList()
    openWindow(dictList)

# Forecasted Weather Output
forecastBtn = tk.Button(
    second_frame, 
    command = callOpenWin, 
    text = "Check Forecast Weather", 
    font = "Sans-serif 10", 
    bg = 'azure3', 
    fg = 'black', 
    activebackground = "lightblue3", 
    padx = 5, 
    pady = 5,
    state=tk.DISABLED
    )
forecastBtn.pack(pady=10)

# Function to retrieve the Activities
def activitiesFunc():
    # creates a new window to display suggested activity.
    top = tk.Toplevel()
    top.grab_set()      # puts the main window on hold until the activity window is closed.
    top.geometry("380x100")
    #top.title("Suggested Activity")
    icon = h.getWeatherIcon()
    activities = Activites(icon)  #Get the activities from the weather icon
    tk.Label(top, text = "Suggested Activities:", font = 'Sans-serif 12 bold').pack(pady = 3)
    text = tk.Text(top, width=300, height=80, font='Sans-serif 10 bold', wrap=tk.WORD)
    text.tag_configure("front_tag", justify ='center')
    text.insert("1.0", activities)
    text.tag_add("front_tag", "1.0", "end")
    text.config(state=tk.DISABLED)
    text.pack()
    def on_closingTop():  
        top.grab_release()      # releases the control so the user can interact with the main window
        top.after(100,lambda:top.destroy())
    top.protocol("WM_DELETE_WINDOW", on_closingTop)

# Button to check the activites that are avaliable
suggestActivityBtn = tk.Button(
    second_frame, 
    command = activitiesFunc, 
    text = "Check Activities Avaliable", 
    font = "Sans-serif 10", 
    bg = 'azure3', 
    fg = 'black', 
    activebackground = "lightblue3", 
    padx = 5, 
    pady = 5,
    state=tk.DISABLED
    )
suggestActivityBtn.pack(pady=10)

# Activities Output
#activities_now = Label(second_frame, text = "Suggested Activities:", font = 'Sans-serif 12 bold').pack(pady = 10)
#activitiesText = Text(second_frame, width = 40, height = 10).pack(pady = 10)

#creates a window using second frame and canvas.
my_canvas.create_window((250,0),window = second_frame, anchor = "n")

# This runs the loop for the window.
# This MUST remain at the end of the file!
window.mainloop()
