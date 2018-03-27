#The next line of code imports the whole Tkinter module
from tkinter import *


class Pascal:
    def __init__(self):

#This line of code is used to create a window

        self.homescreen = Tk()
#The next 4 lines of code sets the title of the window, size of the window and background colour.
#Note: The width and height of the background colour has to be same as that of the screen resolution

        self.homescreen.title("PASCAL")
        self.homescreen.geometry("600x500")

        startBg = Frame(self.homescreen, width=600, height=500, bg="black")
        startBg.pack(side=TOP, expand=NO, fill=NONE)

#Code for the game title and its colour

        gameTitle = Label(self.homescreen, text="PASCAL", fg="steel blue", bg="black", font = "mincho 20 bold")
        gameTitle.place(x=280, y=200)

#Code for Start and Quit buttons


        self.quitButton = Button(self.homescreen, text="Exit", command = self.quitMain, bg="red")
        self.quitButton.place (x=525, y=300)
        

        startButton = Button(self.homescreen, text="Start", bg="green", fg="black")
        startButton.place (x=75, y =300)

    def quitMain(self):
        exit()
        

   

    



        
 
    



        self.homescreen.mainloop()
Pascal()
