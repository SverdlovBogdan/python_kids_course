board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('- - -')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('- - -')
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_chose():
    number = int(input('Введите номер ячейки: '))
    board[number - 1] = 'X'


print_board()
player_chose()
print_board()

