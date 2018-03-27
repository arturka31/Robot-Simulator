import tkinter as tk 

rectanglecolor = 'orange' 
background = tk_rgb = "#%02x%02x%02x" % (100, 255, 100) 
distx = 6 

root = tk.Tk() 
root.geometry('1000x800+0+0') 
root.title("Moving Object Test") 

can = tk.Canvas (root,width=1000,height=800,bg=background) 
can.grid() 

# note that rect is actually just an integer that is used to identifythat shape in the 
# context of the canvas that it was created within. 
rect = can.create_rectangle(400,0,600,200,fill=rectanglecolor) 

for i in range(100): 
# move the rectangle 0 in the x direction and disty in the y direction. 
    can.move(rect, distx, 0) 
    root.update() # update the display 
    root.after(30) # wait 30 ms 

root.mainloop()
