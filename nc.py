print("Hello, welcome to Python Noughts and Crosses!");

board = {"a1":" ","a2":" ","a3":" ","b1":" ","b2":" ","b3":" ","c1":" ","c2":" ","c3":" "}

playerSymbols = ["O","X"]
playerToGo = 0

winner = " "

def printBoard():
	print ("\n==========")
	print "   1  2  3"
	print ("a  " + board["a1"] + "  " + board["a2"] + "  " + board["a3"])
	print ("b  " + board["b1"] + "  " + board["b2"] + "  " + board["b3"])
	print ("c  " + board["c1"] + "  " + board["c2"] + "  " + board["c3"])
	print ("==========")


def takeGo():
	global playerToGo
	global winner
	
	position = raw_input("Type the square you'd like to go in (it's " + playerSymbols[playerToGo] + "'s go): ")
	if position in board :
		if board[position] == " " :
			board[position] = playerSymbols[playerToGo]
			playerToGo = (playerToGo + 1) % 2
			winner = theWinner()
			return
		else :
			print ("That square has already been taken; try again!")
	else :
		print ("That's not a valid square; try again!")
	takeGo()

def theWinner() :
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
	
	
while(winner == " ") :
	printBoard()
	takeGo()
	
print ("\n\n================\n\nThe winner is: " + winner)
printBoard()
