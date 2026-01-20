from piece import Piece
from pawn import Pawn
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
from rook import Rook

class Board:

    # pawn = black : 8, white : 8, id = 1b, 1w
    # rook = black : 2, white : 2, id = 2b, 2w
    # knight = black : 2, white : 2, id = 3b, 3w
    # bishop = black : 2, white : 2, id = 4b, 4w
    # queen = black : 1, white : 1, id = 5b, 5w
    # king = black : 1, white : 1, id = 6b, 6w

    def __init__(self):
        self.pieces = {}
        self.board = [
            ['2.1-b', '3.1-b', '4.1-b', '5-b', '6-b', '4.2-b', '3.2-b', '2.2-b'],
            ['1.1-b', '1.2-b', '1.3-b', '1.4-b', '1.5-b', '1.4-b', '1.3-b', '1.2-b'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['1.1-w', '1.2-w', '1.3-w', '1.4-w', '1.5-w', '1.4-w', '1.3-w', '1.2-w'],
            ['2.1-w', '3.1-w', '4.1-w', '5-w', '6-w', '4.2-w', '3.2-w', '2.2-w']
        ]

    def create_pieces(self):
        for row in self.board:
            for ch in row:
                if ch != '0':
                    self.pieces[ch] = self.create_piece(ch)

    def create_piece(self, ch):
        if ch == '1.1-b':
            return Pawn('black', ch, 1, 0)
        elif ch == '1.2-b':
            return Pawn('black', ch, 1, 1)
        elif ch == '1.3-b':
            return Pawn('black', ch, 1, 2)
        elif ch == '1.4-b':
            return Pawn('black', ch, 1, 3)
        elif ch == '1.5-b':
            return Pawn('black', ch, 1, 4)
        elif ch == '1.6-b':
            return Pawn('black', ch, 1, 5)
        elif ch == '1.7-b':
            return Pawn('black', ch, 1, 6)
        elif ch == '1.8-b':
            return Pawn('black', ch, 1, 7)
        elif ch == '1.1-w':
            return Pawn('black', ch, 6, 0)
        elif ch == '1.2-w':
            return Pawn('black', ch, 6, 1)
        elif ch == '1.3-w':
            return Pawn('black', ch, 6, 2)
        elif ch == '1.4-w':
            return Pawn('black', ch, 6, 3)
        elif ch == '1.5-w':
            return Pawn('black', ch, 6, 4)
        elif ch == '1.6-w':
            return Pawn('black', ch, 6, 5)
        elif ch == '1.7-w':
            return Pawn('black', ch, 6, 6)
        elif ch == '1.8-w':
            return Pawn('black', ch, 6, 7)
        elif ch == '2.1-b':
            return Bishop('black', ch, 0, 0)
        elif ch == '2.2-b':
            return Bishop('black', ch, 0, 7)
        elif ch == '2.1-w':
            return Bishop('white', ch, 7, 0)
        elif ch == '2.2-w':
            return Bishop('white', ch, 7, 7)
        elif ch == "3.1-b":
            return Knight('black', ch, 0, 1)
        elif ch == "3.2-b":
            return Knight('black', ch, 0, 6)
        elif ch == "3.1-w":
            return Knight('white', ch, 7, 1)
        elif ch == "3.2-w":
            return Knight('white', ch, 7, 6)
        elif ch == "4.1-b":
            return Bishop('black', ch, 0, 2)
        elif ch == "4.2-b":
            return Bishop('black', ch, 0, 5)
        elif ch == "4.1-w":
            return Bishop('white', ch, 7, 2)
        elif ch == "4.2-w":
            return Bishop('white', ch, 7, 5)
        elif ch == "5-b":
            return Queen('black', ch, 0, 3)
        elif ch == "5-w":
            return Queen('white', ch, 7, 3)
        elif ch == "6-b":
            return King('black', ch, 0, 4)
        elif ch == "6-w":
            return King('white', ch, 7, 4)

    def print_board(self):
        for row in self.board:
            print(row)
    # row = 0-7, col = 0-7