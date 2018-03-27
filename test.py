import tkinter as tk
import random
from random import randint, choice
import time

scrollX1= 0
scrollY1= 0
scrollX2= 360
scrollY2= 480

root = tk.Tk()

frameWidth=480 #constants for the frame to try make an auto-scrollbar
frameHeight=360 #

frame = tk.Frame(root, width =frameWidth, height =frameHeight)

canvas = tk.Canvas(frame, width = 1000, height=360, bg="green", scrollregion=(scrollX1, scrollY1, scrollX2, scrollY2))

                 
scrollbar = tk.Scrollbar(frame,orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
scrollbar.config(command=canvas.xview)
#canvas.configure(scrollregion=(scrollX1, scrollY1, scrollX2, scrollY2))
frame.grid(row=0,column=0)
canvas.pack()

#x1=340
#x2=360
x1=100
x2=140
y1=365
y2=200
#canvas.create_rectangle(x1,y1,x2,y2, fill = "red", width=2)
#canvas.create_rectangle(400,365,420,200)
def scrollregx1(x):
    x = x + x1
    return x
def scrollregx2(x):
    x = x + x2
    return x

#print(scrollX1,scrollX2)
for i in range(1,500):
    canvas.create_rectangle(x1, choice([0,365]),x2, randint(100,200), fill = "red", width = 2)
    #canvas.create_rectangle(x1, choice([0,365]),x2, randint(100,200), fill = "yellow", width = 2)
    canvas.update()
    time.sleep(0.1)
    x1 = x1 + 120
    x2 = x2 + 120
    scrollX1 = scrollregx1(scrollX1)
    scrollX2 = scrollregx2(scrollX2)
    frame.update()
    root.update()
    """while i < 500:
                 scrollX1 = scrollX1+x1
                 scrollX2 = scrollX2+x2"""
    
    
    """if x1 > frameWidth or x2 > frameWidth:
        frameWidth = frameWidth + 50
        frame.update()"""
    print(x1,x2,scrollX1,scrollX2)


root.mainloop()
