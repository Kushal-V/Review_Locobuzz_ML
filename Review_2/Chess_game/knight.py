from piece import Piece

class Knight(Piece):
    def __init__(self, color, id,row,col):
        super().__init__(color)
        self.id = id
        self.exsited = True
        self.row = row
        self.col = col

    def can_move(self, board, row, col):
        pass