from .PieceMoove import Piece , MoovePiece , isInTab
from .Coordinates import Coordinates as cd, Moove as m , MooveType as mt
from .Screen import drawPoint, moveImg , drawBoard
from .SettingsUpload import br,bn,bb,bq,bk,bp,wp,wr,wn,wb,wq,wk
from .PieceAttribute import PieceType as pt , ColorPlayer as cp

lastMoove = None
PieceSelect = Piece (cd(None,None),None,None,None)
turn = cp.WHITE
cordPromotion=[]


board =[[Piece(cd(0,0),cp.BLACK,pt.ROOK,br),
         Piece(cd(0,1),cp.BLACK,pt.KNIGHT,bn),
         Piece(cd(0,2),cp.BLACK,pt.BISHOP,bb),
         Piece(cd(0,3),cp.BLACK,pt.QUEEN,bq),
         Piece(cd(0,4),cp.BLACK,pt.KING,bk),
         Piece(cd(0,5),cp.BLACK,pt.BISHOP,bb),
         Piece(cd(0,6),cp.BLACK,pt.KNIGHT,bn),
         Piece(cd(0,7),cp.BLACK,pt.ROOK,br)],
        [Piece(cd(1,i),cp.BLACK,pt.PAWN,bp) for i in range (8)],

        8*[None],8*[None],8*[None],8*[None],

        [Piece(cd(6,i),cp.WHITE,pt.PAWN,wp) for i in range (8)],
        [Piece(cd(7,0),cp.WHITE,pt.ROOK,wr),
         Piece(cd(7,1),cp.WHITE,pt.KNIGHT,wn),
         Piece(cd(7,2),cp.WHITE,pt.BISHOP,wb),
         Piece(cd(7,3),cp.WHITE,pt.QUEEN,wq),
         Piece(cd(7,4),cp.WHITE,pt.KING,wk),
         Piece(cd(7,5),cp.WHITE,pt.BISHOP,wb),
         Piece(cd(7,6),cp.WHITE,pt.KNIGHT,wn),
         Piece(cd(7,7),cp.WHITE,pt.ROOK,wr)]]
cp.WHITE

def showBoard() :
    for i in board :
        print("[",end="")
        for j in i :
            print (j,end=", ")
        print("]")
import pygame as py

def changeTurn() :
    global turn
    if turn == cp.WHITE :
        turn = cp.BLACK
    else :
        turn = cp.WHITE

def selectPiece(cord : cd):
    global PieceSelect
    board[cord.y][cord.x].calculateMovements(board,lastMoove)
    PieceSelect = board[cord.y][cord.x]
    drawPoint(PieceSelect.movements, turn,board)
    #print(cd(PieceSelect.y,PieceSelect.x).writeCoordinates())

def moovePiece(cord : cd) -> bool :
    global lastMoove , cordPromotion
    i=0
    canMove = False
    while i<len(PieceSelect.movements) and not canMove:
        pieceSelectMovement = PieceSelect.movements[i];
        if pieceSelectMovement == cord  :
            print(PieceSelect.pieceType()[0]+ " "+ cd(PieceSelect.y,PieceSelect.x).writeCoordinates()+" "+str(pieceSelectMovement))
            MoovePiece(board,PieceSelect,cord, canEat=True)
            moveImg(cord,PieceSelect.img,turn)
            #On déplace une tour ou un roi
            if PieceSelect.type == pt.ROOK or PieceSelect.type == pt.KING:
                PieceSelect.moove = True
            #On fait petit roque
            if pieceSelectMovement.mooveType == mt.CASTLE :
                print (MoovePiece(board,cd(cord.y,7),cd(cord.y,cord.x-1)))
            #On fait grand roque
            if pieceSelectMovement.mooveType == mt.LONGCASTLE :
                MoovePiece(board,cd(cord.y,0),cd(cord.y,cord.x+1))
            #On déplace un pion de 2 cases
            if pieceSelectMovement.mooveType ==  mt.MOOVE2:
                lastMoove = pieceSelectMovement
            else :
                lastMoove  = None
            #On fait une promotion
            if pieceSelectMovement.y ==  7 or  pieceSelectMovement.y  == 0 and PieceSelect.type == pt.PAWN:
                PieceSelect.Promotion(board)
                if turn == cp.WHITE :
                    cordPromotion = [cd(PieceSelect.y,PieceSelect.x),cd(PieceSelect.y+1,PieceSelect.x),cd(PieceSelect.y+2,PieceSelect.x),cd(PieceSelect.y+3,PieceSelect.x)]
                else :
                    cordPromotion = [cd(PieceSelect.y,PieceSelect.x),cd(PieceSelect.y-1,PieceSelect.x),cd(PieceSelect.y-2,PieceSelect.x),cd(PieceSelect.y-3,PieceSelect.x)]
            if board[cord.y][cord.x].thereIsCheck(board) :
                print("échec")
            board[cord.y][cord.x].movements = []
            canMove = True
        i+=1
    return canMove
    

def makePromotion(cord,turn) : 
    piecePromotion = None 
    PicturePiece = None
    if cordPromotion[0] == cord :
        piecePromotion = pt.QUEEN
        if turn == cp.WHITE :
            PicturePiece = wq
        else :
            PicturePiece = bq
    elif cordPromotion[1] == cord :
        piecePromotion =pt.KNIGHT
        if turn == cp.WHITE :
            PicturePiece = wn
        else :
            PicturePiece = bn
    elif cordPromotion[2] == cord :
        piecePromotion = pt.ROOK
        if turn == cp.WHITE :
            PicturePiece = wr
        else :
            PicturePiece = br
    elif cordPromotion[3] == cord :
        piecePromotion = pt.BISHOP
        if turn == cp.WHITE :
            PicturePiece = wb
        else :
            PicturePiece = bb
    if piecePromotion != None :
        print(piecePromotion)
        board[PieceSelect.y][PieceSelect.x].type =piecePromotion
        board[PieceSelect.y][PieceSelect.x].img = PicturePiece


def leftClic (x : int ,y : int ):
    global PieceSelect,lastMoove
    cord = cd(y,x)
    cord = cord.screenToBoard(turn)
    piecePromotion = None
    PieceMoove = False
    if PieceSelect.type == pt.PROMOTION :
        makePromotion(cord,turn)
        drawBoard(board,turn)
        PieceMoove = True
    else : 
        if board[cord.y][cord.x] != None and board[cord.y][cord.x].color == turn :
            selectPiece(cord)
        elif PieceSelect.type != None:
            if not moovePiece(cord) :
                print(PieceSelect.pieceType()[1],PieceSelect.pieceType()[0],"ne peut pas bouger en",cord.writeCoordinates())
            else :
                PieceMoove = True
    if PieceSelect.type != pt.PROMOTION and PieceMoove == True :
        PieceSelect = Piece (cd(None,None),None,None,None)
        changeTurn()
        drawBoard(board,turn)
