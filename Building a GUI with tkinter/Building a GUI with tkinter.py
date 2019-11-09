# -*- coding: utf-8 -*-

"""
Example GUI using tkinter

Tutorial Examples followed: 
https://www.datacamp.com/community/tutorials/gui-tkinter-python#GUI

Color Pallette:
http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
"""

from tkinter import *

import tkinter.messagebox

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon init
    def __init__(self, master=None):

        #Specify parameters that you want to send through the Frame class
        Frame.__init__(self, master)
        #reference to the master widget, which is the tk window  
        self.master = master

        ## run init_window
        self.init_window()
   
    #
    #Creation of init_window
    #   
    def init_window(self):
        #
        # Setting a Title 
        #
        self.master.title("GUI Name")

        # allowing the widget to take the full space of the root window
       # self.pack(fill=BOTH, expand=1)

        # 
        # Set a Label
        #   
        #tkinter.Label(self.master, text = " ", fg = "white", bg = "mediumblue").grid(row = 0, column = 0) 
        #tkinter.Label(self.master, text = "Taking all available X width", fg = "white", bg = "mediumblue").grid(row = 0, column = 1)
        title_label = tkinter.Label(self.master, text = "Title Label", fg = "white", bg = "mediumblue")
        title_label.grid(row = 0, column = 0)

        #
        # Set a button
        #
        button = tkinter.Button(self.master, text = "Quit", command = self.client_exit)
        button.grid(row = 1, column = 0)
        
        
        #
        # creating a menu instance
        #
        menu = Menu(self.master)

        self.master.config(menu=menu)
 
        # create the file object)
        file = Menu(menu)
 
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)     

    def client_exit(self):
        #
        # Exit Event from Menu selection
        #
        # creating a question to get the response from the user [Yes or No Question]
        response = tkinter.messagebox.askquestion("Alert", "Are you sure you want to quit?")

        # If user clicks 'Yes' then it returns 1 else it returns 0
        if response == 'yes':

            root.destroy()

        else:   

            tkinter.Label(self, text = "You stayed!").pack()    

root = Tk()

root.geometry("400x300")

#Create window instance
app = Window(root)

#main loop
root.mainloop()       