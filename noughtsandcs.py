
board = {}

alphabet = ["a","b","c","d","e"]

COLS = 3
ROWS = 3

# Initialize the board
for letter in range(ROWS):
  for number in range(1,COLS+1):
    board[alphabet[letter] + str(number)] = "."

def printBoard(board) :
  print ("\n==========")
  print "   1  2  3"
  print ("a  " + board["a1"] + "  " + board["a2"] + "  " + board["a3"])
  print ("b  " + board["b1"] + "  " + board["b2"] + "  " + board["b3"])
  print ("c  " + board["c1"] + "  " + board["c2"] + "  " + board["c3"])
  print ("==========")