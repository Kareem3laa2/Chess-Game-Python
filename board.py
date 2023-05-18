from const import *
from square import *
from piece import *
from move import Move


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._creat()
        self._add_pieces("white")
        self._add_pieces("black")

    def calc_moves(self, piece, row, col):
        # Calculate all possible moves of an specific piece on a specific position

        def pawn_moves():
            steps = 1 if piece.moved else 2

            # vertical movees
            start = row + piece.dir
            end = row + piece.dir * (1 + steps)
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # creat initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # creat a new move
                        move = Move(initial, final)
                        piece.add_move(move)
                        # blocked piece
                    else:
                        break
                    # not in range
                else:
                    break
            # diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][
                        possible_move_col
                    ].has_enemy_piece(piece.color):
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(inital, final)
                        piece.add_move(move)

        def knight_moves():
            # 8 possible moves for a knight
            possible_moves = [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col + 2),
                (row - 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col - 2),
            ]
            for possible_moves in possible_moves:
                possible_move_row, possible_move_col = possible_moves
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][
                        possible_move_col
                    ].isempty_or_enemy(piece.color):
                        # squares
                        initial = Square(row, col)
                        final = Square(
                            possible_move_row, possible_move_col
                        )  # piece = piece
                        # Creat a new move
                        move = Move(initial, final)
                        # Append a move
                        piece.add_move(move)

        def strightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            piece.add_move(move)

                        if self.squares[possible_move_row][
                            possible_move_col
                        ].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break
                        if self.squares[possible_move_row][
                            possible_move_col
                        ].has_team_piece(piece.color):
                            break

                    else:
                        break
                    # increments
                    possible_move_row, possible_move_col = (
                        possible_move_row + row_incr,
                        possible_move_col + col_incr,
                    )

        def king_moves():
            adjs = [
                (row - 1, col + 0),
                (row - 1, col + 1),
                (row + 0, col + 1),
                (row + 0, col - 1),
                (row + 1, col + 1),
                (row + 1, col - 1),
                (row + 1, col + 0),
                (row - 1, col - 1),
            ]
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][
                        possible_move_col
                    ].isempty_or_enemy(piece.color):
                        # squares
                        initial = Square(row, col)
                        final = Square(
                            possible_move_row, possible_move_col
                        )  # piece = piece
                        # Creat a new move
                        move = Move(initial, final)
                        # Append a move
                        piece.add_move(move)
            # castling moves

            # queen castling
            # ing castling

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            strightline_moves(
                [
                    (-1, +1),
                    (-1, -1),
                    (1, 1),
                    (1, -1),
                ]
            )
        elif isinstance(piece, Rook):
            strightline_moves(
                [
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                    (0, -1),
                ]
            )
        elif isinstance(piece, Queen):
            strightline_moves(
                [
                    (-1, +1),
                    (-1, -1),
                    (1, 1),
                    (1, -1),
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                    (0, -1),
                ]
            )
        elif isinstance(piece, King):
            king_moves()

    def _creat(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # if the color is white then the pawn row and the other is last 2 rows nad if it's black then it's first 2 rows
        if color == "white":
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 0, Bishop(color))
