from .SettingsUpload import side
from .PieceAttribute import PieceType as pt, ColorPlayer as cp
from enum import Enum



class Coordinates :
    def __init__(self,y : int ,x : int) :
        self.y = y
        self.x = x
        
    def writeCoordinates(self) :
        return chr(97+self.x)+str(((self.y+1)*-1 %8)+1)
        
    def inTheBoard(self) :  
        return self.x >=0 and self.x <8 and self.y>=0 and self.y <8
    
    def screenToBoard (self,turn  : cp):
        cord = Coordinates(self.y//side,self.x//side)
        if turn == cp.BLACK :
            cord.reverse()
        return cord

    def boardToScreen(self,turn : cp) :
        cord = Coordinates(self.y,self.x)
        if turn == cp.BLACK :
            cord.reverse()
        cord*side
        return cord
    

    def reverse(self) :
        self.y =((self.y+1)*-1 %8)
        self.x =((self.x+1)*-1 %8)


    def __eq__(self,other) -> bool :

        return self.y == other.y and self.x == other.x 
    
    def __mul__(self,number : int):
        self.y*=number
        self.x*=number

    def __str__(self):
        return str(self.y) + str(self.x)

class MooveType(Enum) :
    EAT = "x"
    MOOVE ="se deplace en"
    MOOVE2 = "se déplace de deux cases en"
    CASTLE = "fait roque"
    LONGCASTLE = "fait Grandroque"
    ENPASSANT = "fait la prise en passant en"
    PROMOTION = "promotion"
    CHECK = "échec"
    
class Moove(Coordinates) :
    def __init__(self,y,x,mooveType : MooveType,pieceEat=None, promotion = False):
        super().__init__(y,x)
        self.mooveType = mooveType
        if MooveType == MooveType.EAT and pieceEat ==None:
            print("Erreur vous devez indiquez la pièce qui est mangé")


    def __eq__(self,other) :
        if other is None:
            return False
        if type (other) == Coordinates :
            return super().__eq__ (other)
        return super().__eq__ (other) and self.mooveType == other.mooveType
    
    def writeMoove(self) :
        return self.moove + chr(97+self.x)+str(self.y)
    
    def __str__(self) :
        result = self.mooveType.value
        return result  + " " + super().writeCoordinates()
    
    def mooveType(self) :
     if self.moove[1] == MooveType.EAT :
          return "mange en"
     else :
          return "se déplace en "
     
def pieceType(character) :
        match character :
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
    