import MinMax


#make a blank board

def newBoard():
	board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
	return board


#put a move on the board

def makeMove(location,curr_board, ai_move):

	#check to see if there isn't already a move made in the 
	if(curr_board[location[0]][location[1]] != '_' ):
		print('IllegalMove')
		return curr_board
	if(not ai_move):
		curr_board[location[0]][location[1]] = 'x'
	else:
		curr_board[location[0]][location[1]] = 'o'


	return curr_board

def getValidMoves(curr_board):
	moves = []
	for i in range(3):
		for j in range(3):
			if(curr_board[i][j]=='_'):
				moves.append([i,j])

	return moves

def isTie(curr_board):
	for i in range(3):
		for j in range(3):
			if(curr_board[i][j] == '_'):
				return False
	return True

def isWin(curr_board):
	for i in range(3):
		if(curr_board[i][0] == 'x' and curr_board[i][1] == 'x' and curr_board[i][2] == 'x'):
			return True
		if(curr_board[0][i] == 'x' and curr_board[1][i] == 'x' and curr_board[2][i] == 'x'):
			return True
	if(curr_board[0][0] == 'x' and curr_board[1][1] == 'x' and curr_board[2][2] == 'x'):
		return True
	if(curr_board[2][0] == 'x' and curr_board[1][1] == 'x' and curr_board[0][2] == 'x'):
		return True

	return False


def isLoss(curr_board):
	for i in range(3):
		if(curr_board[i][0] == 'o' and curr_board[i][1] == 'o' and curr_board[i][2] == 'o'):
			return True
		if(curr_board[0][i] == 'o' and curr_board[1][i] == 'o' and curr_board[2][i] == 'o'):
			return True
	if(curr_board[0][0] == 'o' and curr_board[1][1] == 'o' and curr_board[2][2] == 'o'):
		return True
	if(curr_board[2][0] == 'o' and curr_board[1][1] == 'o' and curr_board[0][2] == 'o'):
		return True

	return False

def isOver(board):
	return isWin(board) or isLoss(board) or isTie(board)

def getUserMove():
	move = []
	yCoord = input("Please enter the 1st coord of your move:\n")
	move.append(int(yCoord))
	xCoord = input("Please enter the 2nd coord of your move:\n")
	move.append(int(xCoord))
	return move


def getCompMove(board):
	return MinMax.getBestMove(board)

def displayBoard(curr_board):
	for i in range(3):
		print(curr_board[i][0] + ' ' + curr_board[i][1] + ' ' + curr_board[i][2] + '\n')

def playGame():
	board = newBoard()
	while(not isOver(board)):
		move = getUserMove()
		board = makeMove(move, board, False)
		displayBoard(board)
		if(isWin(board)):
			print("You Win")
			break
		if(isTie(board)):
			print("Tie game")
			break
		move = getCompMove(board)
		board = makeMove(move, board, True)
		displayBoard(board)
		if(isLoss(board)):
			print('Computer wins')
			break
		




if __name__ == '__main__':
	playGame()








