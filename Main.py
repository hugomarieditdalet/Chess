from ReglesDuJeu.GameTurn import leftClic, board, turn
from ReglesDuJeu.Screen import drawBoard
import pygame as py


run = True
drawBoard(board,"W")
while run :
    for event in py.event.get():
        if event.type == py.QUIT :
            run = False 
        if event.type == py.MOUSEBUTTONDOWN:
            x,y = event.pos
            leftClic(x,y)
py.quit()