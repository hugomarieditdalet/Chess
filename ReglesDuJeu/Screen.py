import pygame as py
from .SettingsUpload import screen,side,numbers, letters , numberSize, pointRadius , promotionBlack , promotionWhite
from .Coordinates import Coordinates as cd
from .PieceAttribute import ColorPlayer as cp

cordsPointsCases = []
cordsPointsPieces = []

def drawSquare(cordBoard,turn) :
    cordScreen = cordBoard.boardToScreen(turn)
    if (cordBoard.y+cordBoard.x)%2 ==0 :
        py.draw.rect (screen,(255,255,255),(cordScreen.x,cordScreen.y,side,side))
    else :
        py.draw.rect (screen,(255,105,150),(cordScreen.x,cordScreen.y,side,side))

def drawPiece(board,cordBoard,turn) :
    cordScreen = cordBoard.boardToScreen(turn)
    if board[cordBoard.y][cordBoard.x] != None :
        screen.blit(board[cordBoard.y][cordBoard.x].img,(cordScreen.x,cordScreen.y))

def drawCoordinates(cordBoard,turn) :
    cordScreen = cordBoard.boardToScreen(turn)
    if turn == cp.BLACK:
        if cordBoard.x == 7 :
            screen.blit(numbers[-cordBoard.y-1],(cordScreen.x,cordScreen.y))
        if cordBoard.y == 0 :
            screen.blit(letters[cordBoard.x],(cordScreen.x+side-numberSize/2,cordScreen.y+side-numberSize/2))
    else :
        if cordBoard.x == 0 :
            screen.blit(numbers[-cordBoard.y-1],(cordScreen.x,cordScreen.y))
        if cordBoard.y == 7 :
            screen.blit(letters[cordBoard.x],(cordScreen.x+side-numberSize/2,cordScreen.y+side-numberSize/2))


def drawBoard(board,turn) :
    global cordsPointsCases,cordsPointsPieces
    for y in range (8) :
        for x in range(8) :
            cordBoard = cd(y,x)
            drawSquare(cordBoard,turn)
            drawPiece(board,cordBoard,turn)
            drawCoordinates(cordBoard,turn)
            cordsPointsCases = []
            cordsPointsPieces = []
            py.display.update()

def delPoint(turn) :
    for cord in cordsPointsCases :
        drawSquare(cord,turn)
    for piece in cordsPointsPieces :
        drawSquare(cd(piece.y,piece.x),turn)
        cordScreen = cd(piece.y,piece.x).boardToScreen(turn)
        screen.blit(piece.img,(cordScreen.x,cordScreen.y))


            

def drawPoint (movements,turn,board):
    global cordsPointsCases , cordsPointsPieces
    delPoint(turn)
    cordsPointsCases = []
    cordsPointsPieces = []
    for cord in movements :
        cordScreen = cord.boardToScreen(turn)
        if board[cord.y][cord.x] == None :
            cordsPointsCases.append(cord)
        else :
            cordsPointsPieces.append(board[cord.y][cord.x])
        py.draw.circle(screen,(0,0,0),(cordScreen.x+side/2,cordScreen.y+side/2),pointRadius)
        py.display.update()

def moveImg (placement,img,turn) :
    cordScreen =  placement.boardToScreen(turn)
    screen.blit(img,(cordScreen.x,cordScreen.y))
    py.display.update()

def drawPromotionInterface(placement,color) :
    cordScreen = placement.boardToScreen(color)
    for i in range (4) :
        py.draw.rect (screen,(255,255,255),(cordScreen.x,cordScreen.y,side,side))
        if color == cp.WHITE :
            screen.blit(promotionWhite[i],(cordScreen.x,cordScreen.y))
        else :
            screen.blit(promotionBlack[i],(cordScreen.x,cordScreen.y))
        cordScreen.y +=side
    py.display.update()

