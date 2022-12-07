# Written by Vedant Patel
# 18 November, 2022
# Interface GUI

#Import the proper libraries
import tkinter as tk   
from tkinter import *
from HelperFile import *
from ForecastWeatherAPI import forecastWeatherAPI
from PIL import ImageTk, Image


def openWindow(Dict):
    h = Helper() 
    topWin = Toplevel()
    topWin.grab_set()      # puts the main window on hold until the activity window is closed.
    topWin.geometry("400x200")
    topWin.title("7-Day Forecast Weather")

    frame = Frame(
        topWin,
        width=400,
        height=200,
        bg = "lightsteelblue2"
    )
    frame.pack(fill = BOTH, expand = 1)
    # Create Frame for X Scrollbar
    sec = Frame(frame) 
    sec.pack(fill = X,side = BOTTOM)

    # Create A Canvas
    my_canvas = Canvas(
        frame,
        width= 400,
        height= 200,
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
        frame, 
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
    #forecast_weather = h.testForecast()
    forecast_weather = Dict
    for dictVal in forecast_weather:
        strValue = h.formatForecastWeather(dictVal)
        tempFrame = Frame(second_frame, width=50, height = 10)
        Label(tempFrame, text=dictVal["date"]).pack(pady=2)
        iconP = "Icons/" + str(dictVal["icon"])
        icon = ImageTk.PhotoImage(Image.open(iconP))
        iconL = Label(tempFrame)
        iconL.configure(image=icon)
        iconL.image = icon
        iconL.pack()
        tempText = Text(tempFrame, width = 36, height= 4, wrap=WORD)
        tempText.insert(INSERT, strValue)
        tempText.pack()
        tempFrame.pack(side=LEFT, padx=10, pady= 15)
    
    my_canvas.create_window((0,0),window = second_frame, anchor = "nw")
                
    def on_closingTop():  
        topWin.grab_release()      # releases the control so the user can interact with the main window
        topWin.after(100,lambda:topWin.destroy())
    topWin.protocol("WM_DELETE_WINDOW", on_closingTop)