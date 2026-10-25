import pygame as py
from .Coordinates import Coordinates as cd

def clicCoord ():
    run = True
    while run :
        for event in py.event.get():
            if event.type == py.QUIT :
                run = False 
            if event.type == py.MOUSEBUTTONDOWN:
                x,y = event.pos
                return cd(x,y)
    py.quit()
    
