from const import *
from square import *
from piece import *
class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._creat()
        self._add_pieces('white')
        self._add_pieces('black')
    def _creat(self):
        

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)


    def _add_pieces(self,color):
        #if the color is white then the pawn row and the other is last 2 rows nad if it's black then it's first 2 rows
        if color == 'white':
            row_pawn, row_other = (6,7)
        else:
            row_pawn,row_other = (1,0)

        #pawns
        for col in range(COLS):
            self.squares[row_pawn][col]=Square(row_pawn,col,Pawn(color))
        #knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other,6,Knight(color))
        #rooks
        self.squares[row_other][0] = Square(row_other,0,Rook(color))
        self.squares[row_other][7] = Square(row_other,7,Rook(color))
        #Queen
        self.squares[row_other][3] = Square(row_other,3,Queen(color))
        #king
        self.squares[row_other][4] = Square(row_other,4,King(color))
        #bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,0,Bishop(color))
