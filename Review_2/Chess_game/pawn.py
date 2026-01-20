from piece import Piece

#board = [
#        ['2.1-b', '3.1-b', '4.1-b', '5-b', '6-b', '4.2-b', '3.2-b', '2.2-b'],
#        ['1.1-b', '1.2-b', '1.3-b', '1.4-b', '1.5-b', '1.4-b', '1.3-b', '1.2-b'],
#        ['0', '0', '0', '0', '0', '0', '0', '0'],
#        ['0', '0', '0', '0', '0', '0', '0', '0'],
#        ['0', '0', '0', '0', '0', '0', '0', '0'],
#        ['0', '0', '0', '0', '0', '0', '0', '0'],
#        ['1.1-w', '1.2-w', '1.3-w', '1.4-w', '1.5-w', '1.4-w', '1.3-w', '1.2-w'],
#        ['2.1-w', '3.1-w', '4.1-w', '5-w', '6-w', '4.2-w', '3.2-w', '2.2-w']
#    ]

class Pawn(Piece):
    def __init__(self, color, id,row,col):
        super().__init__(color)
        self.id = id
        self.exsited = True
        self.row = row
        self.col = col

    def can_move(self, id, board, row, col):
        board[self.row][self.col] = '0'
        self.row = row
        self.col = col
        board[row][col] = id
        return board