# -*- coding: utf-8 -*-

"""

Spyder Editor

 

This is a temporary script file.

"""

 

from tkinter import *

import tkinter.messagebox

 

 

# Here, we are creating our class, Window, and inheriting from the Frame

# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)

#https://www.datacamp.com/community/tutorials/gui-tkinter-python#GUI

class Window(Frame):

   

    # Define settings upon init

    def __init__(self, master=None):

       

        #Specify parameters that you want to send through the Frame class

        Frame.__init__(self, master)

       

        #reference to the master widget, which is the tk window  

        self.master = master

       

        ## run init_window

        self.init_window()

     

    #Creation of init_window

    def init_window(self):

 

        # changing the title of our master widget     

        self.master.title("GUI Name")

 

        # allowing the widget to take the full space of the root window

        self.pack(fill=BOTH, expand=1)

 

       # creating a menu instance

        menu = Menu(self.master)

        self.master.config(menu=menu)

 

        # create the file object)

        file = Menu(menu)

 

        # adds a command to the menu option, calling it exit, and the

        # command it runs on event is client_exit

        file.add_command(label="Exit", command=self.client_exit)

 

        #added "file" to our menu

        menu.add_cascade(label="File", menu=file)

 

        # create the file object)

        edit = Menu(menu)

 

        # adds a command to the menu option, calling it exit, and the

        # command it runs on event is client_exit

        edit.add_command(label="Undo")

 

        #added "file" to our menu

        menu.add_cascade(label="Edit", menu=edit)

      

    def client_exit(self):

        #tkinter.messagebox.showinfo("Alert Message", "Are you sure you want to quit?")

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