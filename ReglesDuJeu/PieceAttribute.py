from enum import Enum

class PieceType(Enum) :
    PAWN = "pion"
    KNIGHT = "cavalier"
    BISHOP = "fou"
    ROOK = "tour"
    QUEEN = "reine"
    KING = "king"
    PROMOTION = "promotion"

class ColorPlayer(Enum) :
    WHITE = "blanc"
    BLACK = "Noir"