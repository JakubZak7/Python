# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]
rows = len(tic_tac_toe_board)
column = len(tic_tac_toe_board[0])

for rowindex in range(0,rows):
   for columnindex in range(0,column):
      print(tic_tac_toe_board[rowindex][columnindex], end=" ")
   print()