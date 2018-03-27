import tkinter as tk
from random import randint, choice
import time


class Grid():
    def __init__(self, width, height, *args):
        self.width = width//10
        self.height = height//10
        self.y = 0
        self.x = 0
        #self.printGrid(self.wallDraw(self.arrayGen()))
        #self.printGrid(self.robot(self.wallDraw(self.arrayGen())))
        #self.wallDraw(self.arrayGen())
        array = self.wallDraw(self.arrayGen())
        self.array = array
        self.test = self.robot()
        # Movement and testing keyboard binds:
        root.bind('<w>', self.moveUp)
        root.bind('<s>', self.moveDown)
        root.bind('<d>', self.moveRight)
        root.bind('<a>', self.moveLeft)
        root.bind('<q>', self.gridBut)
        self.lowOb()



    def arrayGen(self):
        """ Generates and returns a 2D list of width*height size """
        return [[0 for i in range(self.width)] for u in range(self.height)]

    def getArray(self, item):
        """ Some testing stuff, don't know if will keep """
        return item

    def wallDraw(self,array):
        """ Draws 10*10pixel sized walls around the canvas and writes their values into the grid """
        for i in range(0,self.height):
            for j in range(0,self.width):
                if i==0 or i==self.height-1 or j==0 or j==self.width-1:
                    array[i][0] = 1
                    array[i][self.width-1] = 1
                    array[0][j] = 1
                    array[self.height-1][j] = 1

                    canvas.create_rectangle(j*10, i*10, j*10 + 10, i*10+ 10,width=0, fill="yellow")
        return array

    def moveUp(self,event):
        canvas.delete(self.PLAYER)
        if self.array[(self.y - 1) + (self.height//2)][self.x + (self.width//2)] == 1:
            self.y = self.y
        else:
            self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 0
            self.y -= 1
        self.PLAYER = canvas.create_rectangle((self.x + (self.width//2)) * 10, (self.y + (self.height//2)) * 10, ((self.x + (self.width//2)) * 10 + 10), (self.y + (self.height//2)) * 10 + 10, fill="red")
        print("w was pressed") #test
        print(self.y) #test
        self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 2
        tk.Tk.update(root)

    def moveDown(self,event):
        canvas.delete(self.PLAYER)
        if self.array[(self.y + 1) + (self.height//2)][self.x + (self.width//2)] == 1:
            self.y = self.y
        else:
            self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 0
            self.y += 1
        self.PLAYER = canvas.create_rectangle((self.x + (self.width//2)) * 10, (self.y + (self.height//2)) * 10, ((self.x + (self.width//2)) * 10 + 10), (self.y + (self.height//2)) * 10 + 10, fill="red")
        print("s was pressed") #test
        print(self.y) #test
        self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 2
        tk.Tk.update(root)
        
    def moveRight(self,event):
        canvas.delete(self.PLAYER)
        if self.array[self.y + (self.height//2)][(self.x + 1) + (self.width//2)] == 1:
            self.x = self.x
        else:
            self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 0
            self.x += 1
        self.PLAYER = canvas.create_rectangle((self.x+(self.width//2))*10, (self.y+(self.height//2))*10, ((self.x+(self.width//2))*10+10), (self.y+(self.height//2))*10+10, fill="red")
        print("d was pressed") #test
        self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 2
        print(self.x) #test
        tk.Tk.update(root)

    def moveLeft(self,event):
        canvas.delete(self.PLAYER)
        if self.array[self.y + (self.height//2)][(self.x - 1) + (self.width//2)] == 1:
            self.x = self.x
        else:
            self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 0
            self.x -= 1
        self.PLAYER = canvas.create_rectangle((self.x+(self.width//2))*10, (self.y+(self.height//2))*10, ((self.x+(self.width//2))*10+10), (self.y+(self.height//2))*10+10, fill="red")
        print("a was pressed") #test
        self.array[self.y + (self.height//2)][self.x + (self.width//2)] = 2
        print(self.x) #test
        tk.Tk.update(root)

    def gridBut(self,event):
        i=0
        while(i<self.height):
            print(self.array[i])
            i+=1

    def lowOb(self):
        for i in range(self.height):
            for j in range(0,self.width,2):
                #r = (i + 1) // 2
                y = randint(0, (i + 1) // 2)
                for g in range(y):
                    self.array[g][j] = 1
                    canvas.create_rectangle(j * 10, g * 10, j * 10 + 10, g * 10 + 10, width=0, fill="yellow")


    # def obsticles(self):
    #     for i in range(self.height):
    #
    #         # #v = randint(r, self.height)
    #         # for j in range(0,self.width,2):
    #         #     r = (i + 1) // 2
    #         #     y = randint(0, r)
    #         #     for g in range(y):
    #         #         self.array[g][j] = 1
    #         #         canvas.create_rectangle(j * 10, g * 10, j * 10 + 10, g * 10 + 10, width=0, fill="yellow")
    #         for b in range(1,self.width, 2):
    #             d = (i + 1) // 2
    #             v = randint(d, self.height)
    #             print(v)
    #             self.array[v][b] = 1
    #             canvas.create_rectangle(b * 10, v * 10, b * 10 + 10, v * 10 + 10, width=0, fill="yellow")
    #             # for h in range(v):
    #             #     self.array[h][b] = 1
    #             #     canvas.create_rectangle(b * 10, h * 10, b * 10 + 10, h * 10 + 10, width=0, fill="yellow")


    def terrain(self):
        """ Generates random terrain starting from either the y=0 coordinate or y=360 coordinate,
            and return it's values in a 2d list"""
        ut = self.width - 2
        y = choice([0,self.height]) #Randomizes which y coordinate to choose first
        if y == 0: #Excecutes if y=0 was chosen
            for i in range(self.height):
                it = randint(2,10) #Randomized height of terrain
                it1 = it
                it1 = it1-it
                it = it1+it
                ux = ut - i
                for z in range(it):
                    self.array[z][ux]=1
                canvas.create_rectangle((ux)*10,0,(ux)*10+10,it*10+10, width=0, fill="red") #Generates rectangle shapes in the canvas
                canvas.update()
                #time.sleep(0.1)
        elif y != 0: #Excecutes if y2=0 wasn't chosen
            for a in range(self.height):
                it = randint(4,17) #Randomized height of terrain
                it = 36 - it
                ux = ut - a
                for c in range(it, 36):
                        self.array[c][ux]=1
                canvas.create_rectangle((ux)*10,self.height,(ux)*10+10,it*10+10, width=0, fill="red")
                canvas.update()
                #time.sleep(0.1)
        #return self.terrain()


    def robot(self):
        self.array[self.y+(self.height//2)][self.x+(self.width//2)]=2 #initial position for the robot

        self.PLAYER = canvas.create_rectangle((self.x+(self.width//2))*10, (self.y+(self.height//2))*10, ((self.x+(self.width//2))*10+10), (self.y+(self.height//2))*10+10, fill="red")
        print(self.x)

        tk.Tk.update(root)
        time.sleep(0.1)
        return self.array


width = 640
height = 480

root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height, bg = "black")

Grid(width,height) #calls the Grid class, which executes all of the remaining work.



canvas.pack()

root.mainloop()
