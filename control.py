# Here we define how the player will interact with the board

def takeGo(board, playerSymbols, playerToGo):
  position = raw_input("Type the square you'd like to go in (it's " + playerSymbols[playerToGo] + "'s go): ")
  if position in board :
    if board[position] == " " :
      board[position] = playerSymbols[playerToGo]
      playerToGo = (playerToGo + 1) % 2
      winner = theWinner(board)
      return playerToGo, winner
    else :
      print ("That square has already been taken; try again!")
  else :
      print ("That's not a valid square; try again!")
  takeGo()
  
def theWinner(board):
  for column in ["1","2","3"]:
    if board["a"+column] == board["b"+column] == board["c"+column] :
      return board["a"+column]
  for row in ["a","b","c"]:
    if board[row+"1"] == board[row+"2"] == board[row+"3"]:
      return board[row+"1"]
  if board["a1"] == board["b2"] == board["c3"] :
    return board["a1"]
  if board["a3"] == board["b2"] == board["c1"] :
    return board["a3"]

  return " "