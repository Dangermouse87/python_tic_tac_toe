

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