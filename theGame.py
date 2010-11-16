from display import printBoard
from control import takeGo

# The main logic of the game.

print("Hello, welcome to Python Noughts and Crosses!");

# Initialize the board & player symbols etc.
board = {"a1":" ","a2":" ","a3":" ","b1":" ","b2":" ","b3":" ","c1":" ","c2":" ","c3":" "}
playerSymbols = ["O","X"]
playerToGo = 0

global winner
winner = " "

while(winner == " ") :
	printBoard(board)
	playerToGo, winner = takeGo(board, playerSymbols, playerToGo)
	
print ("\n\n================\n\nThe winner is: " + winner)
printBoard(board)
