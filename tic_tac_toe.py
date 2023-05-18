import random
import time

def display_board(board):
    print('\n')
    print('     '+board[1]+'|'+board[2]+'|'+board[3])
    print('     -----')
    print('     '+board[4]+'|'+board[5]+'|'+board[6])
    print('     -----')
    print('     '+board[7]+'|'+board[8]+'|'+board[9])
    print('\n')

def choose_marker():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def first_player():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def open_space(board, position):
    return board[position] == ' '

def full_board_check(board):
    for position in range(1,10):
        if open_space(board, position):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not open_space(board, position):
        position = int(input(turn +': Choose your next position: (1-9): '))
    
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def sleep():
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('....')
    time.sleep(0.5)
    print('\n')

print('Welcome to Tic Tac Toe!')

player1_score = 0
player2_score = 0

while True:
    # Reset the board
    game_board = [' '] * 10
    print('\n')
    player1, player2 = choose_marker()
    print('\n')
    print('Deciding who will go first......')
    sleep()
    turn = first_player()
    
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        playing = True
    else:
        playing = False

    while playing:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1, position)

            if win_check(game_board, player1):
                display_board(game_board)
                print(f'Congratulations! {turn} won the game!')
                player1_score += 1
                print(f'The current score is Player 1 {player1_score} : {player2_score} Player 2')
                print('\n')
                playing = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    print(f'The current score is Player 1 {player1_score} : {player2_score} Player 2')
                    print('\n')
                    playing = False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2, position)

            if win_check(game_board, player2):
                display_board(game_board)
                print(f'Congratulations! {turn} has won the game!')
                player2_score += 1
                print(f'The current score is Player 1 {player1_score} : {player2_score} Player 2')
                print('\n')
                playing = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    print(f'The current score is Player 1 {player1_score} : {player2_score} Player 2')
                    print('\n')
                    playing = False
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break