game_board = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_game_board(values):
    print('\n')
    print(' ' + values[1] + ' | ' + values[2] + ' | ' + values[3])
    print('-----------')
    print(' ' + values[4] + ' | ' + values[5] + ' | ' + values[6])
    print('-----------')
    print(' ' + values[7] + ' | ' + values[8] + ' | ' + values[9])
    print('\n')

def handle_position_input():
    position = 0
    while position not in range(1, 10):
        position = int(input("Select position: "))
        print('Please enter number between 1 and 9')

    return position

def set_position(current_symbol, position):
    if game_board[position] in ('X', 'O'):
        print('position already occupied')
    game_board[position] = current_symbol


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

            position = handle_position_input()
            set_position(current_symbol, position)
            print_game_board(game_board)

game()