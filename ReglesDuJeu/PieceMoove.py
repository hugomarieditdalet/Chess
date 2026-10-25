from ReglesDuJeu.Coordinates import Coordinates,Moove,MooveType as mt
from .PieceAttribute import PieceType as pt, ColorPlayer as cp
from .Screen import drawPromotionInterface;

class Piece :
    def __init__(self,cord,color,pieceType,img):
        self.y = cord.y
        self.x = cord.x
        self.color = color
        self.type = pieceType
        self.img = img
        self.movements = []
        if self.type == pt.ROOK or self.type == pt.KING :
            self.moove = False

    
    def __str__(self):
        return str(self.y)+str(self.x)+str(self.color)+str(self.type)
    
    def calculateMovements(self,board,lastMove = None, simulation = False):
        self.movements = []
        #print("simulation : ", simulation)
        match self.type :
            case pt.PAWN:
                self.movementsPawn(board,lastMove)
            case pt.ROOK:
                self.movementsRook(board)
            case pt.BISHOP:
                self.movementsBishop(board)
            case pt.KNIGHT:
                self.movementsKnight(board)
            case pt.QUEEN:
                self.movementsQueen(board)
            case pt.KING:
                self.movementsKing(board,simulation)
        if simulation == False :
            self.retireIllegalMoov(board)

            
    def movementsPawn (self,board,lastMove):
        if self.color == cp.WHITE :
            pawnDirection= -1
        else :
            pawnDirection= 1
        #print("self.y : ", self.y ,"pawn direction" , pawnDirection)
        #déplacement du pion
        if board[self.y+pawnDirection][self.x] == None :
            self.movements.append(Moove(self.y+pawnDirection,self.x,mt.MOOVE))
            #déplacement du pion de 2 cases
            if self.y ==pawnDirection%7 and board[self.y+2*pawnDirection][self.x] == None :
                self.movements.append(Moove(self.y+2*pawnDirection,self.x,mt.MOOVE2))
        #Mager un pièce
        if Coordinates(self.y+pawnDirection,self.x+1).inTheBoard() and board[self.y+pawnDirection][self.x+1] !=None and board[self.y+pawnDirection][self.x+1].color != self.color:
            if board[self.y+pawnDirection][self.x+1].pieceType == pt.KING :
                self.movements.append(Moove(self.y+pawnDirection,self.x+1,mt.CHECK,board[self.y+pawnDirection][self.x+1].pieceType))
            else :
                self.movements.append(Moove(self.y+pawnDirection,self.x+1,mt.EAT,board[self.y+pawnDirection][self.x+1].pieceType))
        if Coordinates(self.y+pawnDirection,self.x-1).inTheBoard() and board[self.y+pawnDirection][self.x-1] !=None and board[self.y+pawnDirection][self.x-1].color != self.color:
            if board[self.y+pawnDirection][self.x-1].type == pt.KING :
                self.movements.append(Moove(self.y+pawnDirection,self.x-1,mt.CHECK,board[self.y+pawnDirection][self.x+1].pieceType))
            else :
                self.movements.append(Moove(self.y+pawnDirection,self.x-1,mt.EAT,board[self.y+pawnDirection][self.x-1].pieceType))
        #En passant
        if self.y == 4*pawnDirection%7 :
            if lastMove == Moove(self.y,self.x+1,mt.MOOVE2):
                self.movements.append(Moove(self.y+pawnDirection,self.x+1,mt.ENPASSANT))
            elif lastMove == Moove(self.y,self.x-1,mt.MOOVE2):
                self.movements.append(Moove(self.y+pawnDirection,self.x-1,mt.ENPASSANT))
        #Promotion
        #if self.color == cp.WHITE and self.y == 7 :
        #    self.movements.append(Moove(self.y+pawnDirection,self.x,mt.PROMOTION))
        #elif self.color == cp.BLACK and self.y ==0 :
        #    self.movements.append(Moove(self.y+pawnDirection,self.x,mt.PROMOTION))

    def Promotion(self,board) :
        print("PROMOTIOn")
        drawPromotionInterface(Coordinates(self.y,self.x),self.color)
        self.type = pt.PROMOTION

            
    def movementsKnight(self,board) :
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i)+abs(j)==3 and Coordinates(self.y+i,self.x+j).inTheBoard() :

                    if board[self.y+i][self.x+j] ==None :
                        self.movements.append(Moove(self.y+i,self.x+j,mt.MOOVE))

                    elif board[self.y+i][self.x+j].color !=self.color :
                        if board[self.y+i][self.x+j].type == pt.KING :
                            self.movements.append(Moove(self.y+i,self.x+j,mt.CHECK,board[self.y+i][self.x+j].pieceType))
                        else :
                            self.movements.append(Moove(self.y+i,self.x+j,mt.MOOVE,board[self.y+i][self.x+j].pieceType))
                        
    def movementsBishop(self,board) :
        for i in range(4) :
            y=self.y
            x=self.x
            stop = False
            while(not stop):
                match i :
                    case 0:
                        x+=1
                        y+=1
                    case 1 :
                        x-=1
                        y-=1
                    case 2 :
                        x+=1
                        y-=1
                    case 3 :
                        x-=1
                        y+=1
                stop = self.CheckSquares(board,y,x)
                
    def movementsRook(self,board) :
        for i in range(4) :
            y=self.y
            x=self.x
            stop = False
            while(not stop):
                match i :
                    case 0 :
                        y+=1
                    case 1 :
                        y-=1
                    case 2 :
                        x+=1
                    case 3 :
                        x-=1
                stop = self.CheckSquares(board,y,x)
                
    def movementsQueen(self,board) :
        self.movementsBishop(board)
        self.movementsRook(board)
    
    def CheckSquares(self,board,y,x) :
        stop = False
        if Coordinates(y,x).inTheBoard():
            if board[y][x] == None:
                self.movements.append(Moove(y,x,mt.MOOVE))
            else :
                if board[y][x].color != self.color :
                    if board[y][x].type == pt.KING :
                        self.movements.append(Moove(y,x,mt.CHECK,board[y][x].pieceType))
                    else :
                        self.movements.append(Moove(y,x,mt.EAT,board[y][x].pieceType))
                stop = True
        else :
            stop = True
        return stop
    
    def movementsKing(self,board, simulation):
        #moov 
        for i in range(-1,2) :
            for j in range(-1,2) :
                if Coordinates(self.y+i,self.x+j).inTheBoard():
                    if board[self.y+i][self.x+j] == None :
                        self.movements.append(Moove(self.y+i,self.x+j,mt.MOOVE))
                    elif board[self.y+i][self.x+j].color != self.color :
                        if board[self.y+i][self.x+j].type== pt.KING :
                            self.movements.append(Moove(self.y+i,self.x+j,mt.CHECK,board[self.y+i][self.x+j].pieceType))
                        else :
                            self.movements.append(Moove(self.y+i,self.x+j,mt.EAT,board[self.y+i][self.x+j].pieceType))

        if simulation == False :
        #Castle
            self.canCastle(board,1) 
            self.canCastle(board,-1)


    def canCastle (self,board,direction) :
        kingLines = 0
        rowRook = 7
        if self.color == cp.WHITE :
            kingLines = 7
        if direction ==-1 :
            rowRook = 0
        canCastle = True
        if board[kingLines][rowRook] != None and board[kingLines][rowRook].moove == False and not KingInDanger(board, self.color) and self.moove == False :
            boardDuplicate = duplicateBoard(board)
            for i in range (1,3) :
                if MoovePiece(boardDuplicate,Coordinates(self.y,self.x+direction*(i-1)),Coordinates(self.y,self.x+direction*i)) : 
                    if (KingInDanger(boardDuplicate, self.color)):
                        canCastle = False
                        break
                else :
                    canCastle = False
                    break
            if canCastle :
                if direction == 1 :
                    self.movements.append(Moove(self.y,self.x+direction*2,mt.CASTLE))
                else :
                    self.movements.append(Moove(self.y,self.x+direction*2,mt.LONGCASTLE))

    def thereIsCheck(self, board) -> bool :
        self.calculateMovements(board)
        for i in self.movements :
            if i.mooveType == mt.CHECK :
                return True
        return False
    
    def retireIllegalMoov(self,board) :
        index = 0
        while index < len(self.movements) :
            cord = self.movements[index]
            boardDuplicate = duplicateBoard(board)
            MoovePiece (boardDuplicate,Coordinates(self.y,self.x),cord)
            if KingInDanger(boardDuplicate,self.color):
                self.movements.remove(cord)
            else :
                index +=1
            


    def pieceType(self) :
        match self.type :
            case pt.PAWN:
                return "pion","Le"
            case pt.ROOK:
                return "tour","La"
            case pt.BISHOP:
                return "fou","Le"
            case pt.KNIGHT:
                return "cavalier","Le"
            case pt.QUEEN:
                return "reine","La"
            case pt.KING:
                return "roi","Le"
            
def KingInDanger(board,color) -> bool :
    for ligne in board :
        for piece in ligne :
            if piece != None and piece.color != color :
                piece.calculateMovements(board,lastMove = None, simulation = True)
                for i in piece.movements :
                    if i.mooveType == mt.CHECK :
                        return True
    return False



def MoovePiece (board,cordPiece,newCordPiece ,canEat = False):
    if board[newCordPiece.y][newCordPiece.x] == None or canEat :
        board[newCordPiece.y][newCordPiece.x] = board[cordPiece.y][cordPiece.x]
        board[cordPiece.y][cordPiece.x] = None
        board[newCordPiece.y][newCordPiece.x].y = newCordPiece.y
        board[newCordPiece.y][newCordPiece.x].x = newCordPiece.x
        return True
    return False
                        
def isInTab(controlSquares,coord):
    estDansTab = False
    i=0
    while not estDansTab and i<len(controlSquares):
        if controlSquares[i] ==coord :
            estDansTab = True
        i+=1
    return estDansTab
        
def duplicateBoard(board) :
    boardDuplicate = []
    for ligne in  board :
        ligneDuplicate = []
        for square in ligne :
            if square == None :
                ligneDuplicate.append(square)
            else :
                ligneDuplicate.append(Piece(Coordinates(square.y,square.x),square.color,square.type,square.img))
        boardDuplicate.append(ligneDuplicate)
    return boardDuplicate

                    
                    
                
                
            
                
                
            

    
    
    