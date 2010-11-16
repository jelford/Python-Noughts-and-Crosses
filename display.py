# Here we define the way we show the board to the player

def printBoard(board):
  print ("\n==========")
  print "   1  2  3"
  print ("a  " + board["a1"] + "  " + board["a2"] + "  " + board["a3"])
  print ("b  " + board["b1"] + "  " + board["b2"] + "  " + board["b3"])
  print ("c  " + board["c1"] + "  " + board["c2"] + "  " + board["c3"])
  print ("==========")