print('**********************************')
print('    Welcome to TIC TAC TOE  !!!   ')
print('**********************************')

#####################################################################
#Defining player input marker
def player_input():
	marker = ''
	
	while not ( marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O?').upper()
	
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')
		
#####################################################################
		

#####################################################################
#Defining the First player		
import random
def chooose_first():
	if random.randint(0,1) == 0:
		return 'Player2'
	else:
		return 'Player1'
		
#####################################################################
		

#####################################################################		
# defining the board
def display_board(board):

	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	
#####################################################################
	

#####################################################################
# Checking for Available space
def space_check(board, position):
	
	return board[position] == ' '
	
#####################################################################

#####################################################################
# Checking if Board is full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True
	
#####################################################################


#####################################################################
#Defining function to place marker
def place_marker(board, marker, position):
	board[position] = marker

#####################################################################


#####################################################################
# Checking the win condition
def win_check(board, mark):
	
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
			(board[4] == mark and board[5] == mark and board[6] == mark) or 
			(board[1] == mark and board[2] == mark and board[3] == mark) or 
			(board[7] == mark and board[4] == mark and board[1] == mark) or 
			(board[8] == mark and board[5] == mark and board[2] == mark) or 
			(board[9] == mark and board[6] == mark and board[3] == mark) or
			(board[7] == mark and board[5] == mark and board[3] == mark) or
			(board[9] == mark and board[5] == mark and board[1] == mark))
#####################################################################
	
#####################################################################	
# Defining position on the Board
def player_choice(board):
	position = 0
	
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose your next position: (1-9) '))
		return position
#####################################################################
# Asking for Replay
def replay():
	return input('Do you want to play again? Yes or No: ').lower().startswith('y')
	
#####################################################################
#					Main Functionality of Game		
#####################################################################
while True:
	theBoard = [' ']*10
	player1_marker, player2_marker = player_input()
	
	turn = chooose_first()
	print(turn + ' will play first')
	
	play_game = input('Ready to play? Enter Yes or No:')
	
	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False
		
	while game_on:
		if turn == 'Player1':
			# Player1's turn
			
			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)
			
			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print('Congratulations! Player1, you have won the game!')
				game_on = False
				
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('the game is draw!')
					break
				else:
					turn = 'Player2'
				
			
			
			
		else:
			# Player2's turn 
			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)
			
			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print('Congratulations! Player2, you have won the game!')
				game_on = False
				
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('the game is draw!')
					break
				else:
					turn = 'Player1'
					
# ASking for replay
	if not replay():
		break