



#Sound Button
play = lambda:windsound.PlaySound("c:\Game.wav", winsound.SND_FILENAME)
soundbutton = Button(gui.frame, text = 'Music',font = ("Arial",10,"bold"), fg = 'black', command = play)
soundbutton.pack(side = LEFT)
