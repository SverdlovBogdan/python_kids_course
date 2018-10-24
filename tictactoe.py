board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
WIN = 1
DRAW = 2
NOTHING = 3

TURN_NUMBERS = 0

def print_board():
    print('')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('- - -')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('- - -')
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_choose(symbol):
    all_numbers = '1 2 3 4 5 6 7 8 9'

    number = input('Введите номер ячейки для %s: ' % symbol)
    number_int = int(number)

    while number not in all_numbers or board[number_int - 1] not in all_numbers:
        print('Некорретный номер ячейки')
        number = input('Введите номер ячейки для %s: ' % symbol)
        number_int = int(number)
    
    board[number_int - 1] = symbol
    global TURN_NUMBERS
    TURN_NUMBERS = TURN_NUMBERS + 1


# def player_o_choose():
#     all_numbers = '1 2 3 4 5 6 7 8 9'

#     number = input('Введите номер ячейки для O: ')
#     number_int = int(number)

#     while number not in all_numbers or board[number_int - 1] not in all_numbers:
#         print('Некорретный номер ячейки')
#         number = input('Введите номер ячейки для O: ')
#         number_int = int(number)
    
#     board[number_int - 1] = 'O'
#     global TURN_NUMBERS
#     TURN_NUMBERS = TURN_NUMBERS + 1

def check_win(symbol):
    # проверка горизонталей
    if symbol == board[0] and board[0] == board[1] and board[1] == board[2]:
        return WIN
    if symbol == board[3] and board[3] == board[4] and board[4] == board[5]:
        return WIN
    if symbol == board[6] and board[6] == board[7] and board[7] == board[8]:
        return WIN
    
    # проверка вертикалей
    if symbol == board[0] and board[0] == board[3] and board[3] == board[6]:
        return WIN
    if symbol == board[1] and board[1] == board[4] and board[4] == board[7]:
        return WIN
    if symbol == board[2] and board[2] == board[5] and board[5] == board[8]:
        return WIN

    # Проверка диагоналей
    if symbol == board[0] and board[0] == board[4] and board[4] == board[8]:
        return WIN
    if symbol == board[2] and board[2] == board[4] and board[4] == board[6]:
        return WIN
    
    return NOTHING

round = 0
player_win = 0
while TURN_NUMBERS < 9:
    print_board()
    player_choose('X')
    print_board()

    if check_win('X') == WIN:
        print('X победили')
        player_win = 1
        break

    if TURN_NUMBERS == 9:
        break
    
    player_choose('O')
    print_board()

    if check_win('O') == WIN:
        print('O победили')
        player_win = 1
        break
    round = round + 1
    print('')
    print('%s Раунд окончен' % str(round))

if TURN_NUMBERS == 9 and player_win == 0:
    print('Ничья!')

