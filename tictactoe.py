board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('- - -')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('- - -')
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_x_choose():
    all_numbers = '1 2 3 4 5 6 7 8 9'

    while True:
        number = input('Введите номер ячейки для X: ')
        
        if number not in all_numbers or board[int(number) - 1] not in all_numbers:
            print('Неверный номер ячейки или ячейка уже занята')
            continue
        else:
            board[int(number) - 1] = 'O'
            break

    board[int(number) - 1] = 'X'

def player_o_choose():
    all_numbers = '1 2 3 4 5 6 7 8 9'
    
    while True:
        number = input('Введите номер ячейки для О: ')

        if number not in all_numbers or board[int(number) - 1] not in all_numbers:
            print('Неверный номер ячейки или ячейка уже занята')
            continue
        else:
            board[int(number) - 1] = 'O'
            break

print_board()
player_x_choose()
print_board()
player_o_choose()
print_board()


