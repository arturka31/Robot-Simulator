#The next line of code imports the whole Tkinter module

from tkinter import *

root = Tk()

class robotPosition():
    def __init__(self, location):
        self.label = location
        location.bind('<ButtonPress-1>', self.StartMove)
        location.bind('<ButtonRelease-1>', self.StopMove)
        self.positions = {}

    def StartMove(self, event):
        startx = event.x
        starty = event.y
        self.positions['start'] = (startx, starty)

    def StopMove(self, event):
        stopx = event.x
        stopy = event.y
        self.positions['stop'] = (stopx, stopy)

# This calculates the distance using the formula

    def distancetraveled(self):
        x1 = self.positions['start'][0]
        x2 = self.positions['stop'][0]
        y1 = self.positions['start'][1]
        y2 = self.positions['stop'][1]
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

location = Canvas(root, width = 300, height = 300)
robotPosition(location)
location.pack()
root.mainloop()

