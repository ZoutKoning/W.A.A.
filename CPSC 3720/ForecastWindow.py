# Written by Vedant Patel

#Import the proper libraries
import tkinter as tk   
from tkinter import *
from HelperFile import *
from PIL import ImageTk, Image


def openWindow(Dict):
    h = Helper() 
    topWin = tk.Toplevel()    #creating main window for forecast window
    topWin.grab_set()      # puts the main window on hold until the forecast window is closed.
    topWin.geometry("400x200")
    topWin.title("7-Day Forecast Weather")

    frame = tk.Frame(
        topWin,
        width=400,
        height=200,
        bg = "lightsteelblue2"
    )
    frame.pack(fill = tk.BOTH, expand = 1)
    # Create Frame for X Scrollbar
    sec = tk.Frame(frame) 
    sec.pack(fill = tk.X,side = tk.BOTTOM)

    # Create A Canvas
    my_canvas = tk.Canvas(
        frame,
        width= 400,
        height= 200,
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
        frame, 
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
    #forecast_weather = h.testForecast()
    forecast_weather = Dict
    # for each day in the forecast json dict do the following:
    # which is adding day label, weather icon, and weather info. 
    for dictVal in forecast_weather:
        # formats the weather info into well formatted text. 
        strValue = h.formatForecastWeather(dictVal)
        # creates a frame around the info for each day.
        tempFrame = tk.Frame(second_frame, width=50, height = 10)
        # date label
        tk.Label(tempFrame, text="Date: "+ dictVal["date"]).pack(pady=2)
        # weather icon
        iconP = "Icons/" + str(dictVal["icon"])
        icon = ImageTk.PhotoImage(Image.open(iconP))
        # creates a label to put the image in. 
        iconL = tk.Label(tempFrame)
        iconL.configure(image=icon)
        iconL.image = icon
        iconL.pack()
        # creates a text field for weather info. 
        tempText = tk.Text(tempFrame, width = 36, height= 4, wrap=tk.WORD)
        tempText.insert(tk.INSERT, strValue)
        tempText.pack()
        tempText.configure(state=tk.DISABLED)
        tempFrame.pack(side=tk.LEFT, padx=10, pady= 15)
    
    # creates the window using the frames. 
    my_canvas.create_window((0,0),window = second_frame, anchor = "nw")

    # upon closing, releases the hold of the main window/app and destorys the forecast window
    def on_closingTop():  
        topWin.grab_release()      # releases the control so the user can interact with the main window
        topWin.after(100,lambda:topWin.destroy())
    # calls on_closingTop function when the "X" button is clicked to close the window. 
    topWin.protocol("WM_DELETE_WINDOW", on_closingTop)