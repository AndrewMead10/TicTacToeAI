import tictactoe as tic


def getBestMove(board):
	best_score = -100
	best_move = []
	temp_board = copyBoard(board)
	for move in tic.getValidMoves(board):
		temp_board = tic.makeMove(move, temp_board, True)
		score = minMax(temp_board, False, -100, 100)
		if(score > best_score):
			best_score = score
			best_move = move
		temp_board[move[0]][move[1]] = '_'
		
	
	return best_move


def minMax(curr_board, ai_turn, alpha, beta):

	

	score = getScore(curr_board)
	temp_board = copyBoard(curr_board)


	if(tic.isOver(curr_board)):
		#tic.displayBoard(curr_board)
		#print(score)
		return score

	if(ai_turn):
		best = -100
		for move in tic.getValidMoves(curr_board):
			temp_board = tic.makeMove(move, temp_board, True)
			best = max(best, minMax(temp_board,False,alpha,beta))
			alpha = max(alpha, best)
			if(beta <= alpha):
				break
			temp_board[move[0]][move[1]] = '_'
		return best
	else:
		best = 100
		for move in tic.getValidMoves(curr_board):
			temp_board = tic.makeMove(move, temp_board, False)
			best = min(best, minMax(temp_board,True,alpha,beta))
			beta = min(best, beta)
			if(beta <= alpha):
				break
			temp_board[move[0]][move[1]] = '_'
		return best




def getScore(curr_board):
	if(tic.isWin(curr_board)):
		return -10
	if(tic.isLoss(curr_board)):
		return 10

	return 0 


def copyBoard(board):
	new_board = tic.newBoard()
	for i in range(3):
		for j in range(3):
			if(board[i][j] != '_'):
				new_board[i][j] = board[i][j]
	return new_board












