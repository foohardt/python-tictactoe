game_board = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_game_board(values):
    print('\n')
    print(' ' + values[1] + ' | ' + values[2] + ' | ' + values[3])
    print('-----------')
    print(' ' + values[4] + ' | ' + values[5] + ' | ' + values[6])
    print('-----------')
    print(' ' + values[7] + ' | ' + values[8] + ' | ' + values[9])
    print('\n')

def handle_position_input(current_symbol):
    position = 0
    while position not in range(1, 10) or not occupied(position):
        position = int(input(current_symbol + ' select position: '))
        print('Please enter number between 1 and 9')

    return position

def occupied(position):
    if game_board[position] in ('X', 'O'):
        print('Position already occupied.')
        return False
    return True

def set_position(current_symbol, position):
    if game_board[position] in ('X', 'O'):
        print('position already occupied')
    game_board[position] = current_symbol

def current_player_is_winner(current_symbol):
    return ((game_board[1] == current_symbol and game_board[2] == current_symbol and game_board[3] == current_symbol) or  # top row
            (game_board[4] == current_symbol and game_board[5] == current_symbol and game_board[6] == current_symbol) or  # middle row
            (game_board[7] == current_symbol and game_board[8] == current_symbol and game_board[9] == current_symbol) or  # bottom row
            (game_board[1] == current_symbol and game_board[4] == current_symbol and game_board[7] == current_symbol) or  # first column
            (game_board[2] == current_symbol and game_board[5] == current_symbol and game_board[8] == current_symbol) or  # second column
            (game_board[3] == current_symbol and game_board[6] == current_symbol and game_board[9] == current_symbol) or  # third column
            (game_board[1] == current_symbol and game_board[5] == current_symbol and game_board[9] == current_symbol) or  # diagonal
            (game_board[3] == current_symbol and game_board[5] == current_symbol and game_board[7] == current_symbol))  # diagonal
    
def game_board_is_full():
    for i in range(1, 10):
        if game_board[i] not in ('X', 'O'):
            return False
    return True

def game():
    while True:
        player_one = 'X'
        player_two = 'O'
        current_turn = 'player_one'
        current_symbol = ''
        print_game_board(game_board)
        while True:
            if current_turn == 'player_one':
                current_symbol = player_one
            else:
                current_symbol = player_two

            position = handle_position_input(current_symbol)
            set_position(current_symbol, position)
            print_game_board(game_board)
            if current_player_is_winner(current_symbol):
                print('Congratulations!' + ' ' + current_symbol + ' ' + 'has won.')
                break
            if game_board_is_full():
                print('Board is full. Please restart game.')
                break
            else:
                current_turn = 'player_two' if current_turn is 'player_one' else 'player_one'
        break

game()