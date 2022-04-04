
# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def show_board(board):
    b = [board[i] if board[i] else str(i) for i in range(0, 10)]
    print(f'{b[1]}┃{b[2]}┃{b[3]}')
    print('━╋━╋━')
    print(f'{b[4]}┃{b[5]}┃{b[6]}')
    print('━╋━╋━')
    print(f'{b[7]}┃{b[8]}┃{b[9]}')

# Function for... (choosing a player?)
def choose_player_turn(board, counter):
    if counter % 2 == 0:
        player_type = 'X'
    else:
        player_type = 'O'
    next_move = int(input('Player %s\'s turn; enter a number in [1..9]: ' % player_type))
    while board[next_move] != '':
        next_move = int(input('the cell %s is already occupied, try another number: ' % next_move))
    board[next_move] = player_type
    show_board(board)
    return next_move


def are_the_indices_a_match(board, i1, i2, i3):
    """
    >>> are_the_indices_a_match(['', 'X', 'X', 'X'], 1, 2, 3)
    True
    """
    if board[i1] not in ['X', 'O']:
        return False
    return board[i1] is board[i2] and board[i2] is board[i3]


def is_there_winner(board):
    """
    >>> is_game_over(['', 'X', 'X', 'X', '', '', '', '', '', ''])
    True
    >>> is_game_over(['', 'X', '', '', 'X', '', '', 'X', '', ''])
    True
    >>> is_game_over(['', 'X', '', '', '', 'X', '', '', '', 'X'])
    True
    """
    game_ended = False
    for i in [1, 4, 7]:
        if are_the_indices_a_match(board, i, i+1, i+2):
            game_ended = True
    for i in [1, 2, 3]:
        if are_the_indices_a_match(board, i, i+3, i+6):
            game_ended = True
    if are_the_indices_a_match(board, 1, 5, 9):
            game_ended = True
    if are_the_indices_a_match(board, 3, 5, 7):
            game_ended = True
    return game_ended

def play_game():
    board = ['']*10
    show_board(board)
    for counter in range(9):
        next_move = choose_player_turn(board, counter)
        if is_there_winner(board):
            winner = 'X' if counter % 2 == 0 else 'O'
            print(f'The game is over! Player {winner} is the winner')
            break
    if not is_there_winner(board):
        print('The game is over. Draw!')
    



# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    play_game()
    # board = ['']*10
    # show_board(board)
    # for counter in range(9):
    #     next_move = choose_player_turn(board, counter)
    #     if is_there_winner(board):
    #         winner = 'X' if counter % 2 == 0 else 'O'
    #         print(f'The game is over! Player {winner} is the winner')
    #         break
    # if not is_there_winner(board):
    #     print('The game is over. Draw!')
    
