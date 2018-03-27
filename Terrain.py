import tkinter as tk
from random import randint, choice
import time

class Grid():
    def __init__(self, width, height, *args):
        self.height = height
        self.width = width

    def gen2dArray(self):
        """ Function for generating 2 dimensional lists """
        array = [[0 for i in range(self.width)] for u in range(self.height)]
        return array
  
    def drawWalls(self, array):
        """ Function, which draws top and bottom walls in the canvas,
            while assigning their values to a 2D list"""
        for u in range(int(self.width)):
                array[0][u] = 1
                array[self.height-1][u] = 1
                walltop = canvas.create_rectangle(u*10,0*10,u*10+10,0*10+10,width=0, fill="red")
                wallbot = canvas.create_rectangle(u*10,self.height*10-5, u*10+10, self.height*10-5+10, width=0, fill="red")
                u+=1
        return array
        
    def terrain(self,array):
        """ Generates random terrain starting from either the y=0 coordinate or y=360 coordinate,
            and return it's values in a 2d list"""
        ut = 48
        y = choice([0,360]) #Randomizes which y coordinate to choose first
        if y == 0: #Excecutes if y=0 was chosen
            for i in range(1,50):
                it = randint(2,10) #Randomized height of terrain
                it1 = it
                it1 = it1-it
                it = it1+it
                ux = ut - i
                for z in range(it):
                    array[z][ux]=1
                canvas.create_rectangle((ux)*10,0,(ux)*10+10,it*10+10, width=0, fill="red") #Generates rectangle shapes in the canvas
                canvas.update()
                time.sleep(0.1)
        elif y != 0: #Excecutes if y2=0 wasn't chosen
            for a in range(1,50):
                it = randint(4,17) #Randomized height of terrain
                it = 36 - it
                ux = ut - a
                for c in range(it, 36):
                        array[c][ux]=1
                canvas.create_rectangle((ux)*10,360,(ux)*10+10,it*10+10, width=0, fill="red")
                canvas.update()
                time.sleep(0.1)
        return array


width = 480
height = 360

root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height, bg = "grey")
canvas.pack()
            

array = Grid(width//10,height//10)
array1 = array.gen2dArray()
array2=array.drawWalls(array1)
while True:
    array3=array.terrain(array2)



