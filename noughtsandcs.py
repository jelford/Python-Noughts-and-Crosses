
board = {}

alphabet = ["a","b","c","d","e"]

COLS = 3
ROWS = 3

# Initialize the board
for letter in range(ROWS):
  for number in range(1,COLS+1):
    board[alphabet[letter] + str(number)] = " "

