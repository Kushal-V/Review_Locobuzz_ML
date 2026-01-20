from board import Board
from pawn import Pawn

board = Board()
board.create_pieces()

while True:
    print("Welcome to Chess Game")
    print("This is the board")
    board.print_board()
    print("White's turn")
    print("Select id to move")
    id = input()
    print("Select position to move")
    position = input()
    row = position.split(' ')[0]
    col = position.split(' ')[1]
    row = int(row)
    col = int(col)
    if id in board.pieces:
        current_piece = board.pieces[id]
        current_piece.can_move(id,board.board,row,col)
    board.print_board()
    
    print("Black's turn")
    print("Select id to move")
    id = input()
    print("Select position to move")
    position = input()
    row = position.split(' ')[0]
    col = position.split(' ')[1]
    row = int(row)
    col = int(col)
    if id in board.pieces:
        current_piece = board.pieces[id]
        current_piece.can_move(id,board.board,row,col)
    board.print_board()

    print("Game Over")
    break