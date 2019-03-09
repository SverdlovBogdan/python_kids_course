board = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
]

def printBoard(ourBoard):
    print(ourBoard[0] + '|' + ourBoard[1] + '|' + ourBoard[2])
    print("- - -")
    print(ourBoard[3] + '|' + ourBoard[4] + '|' + ourBoard[5])
    print("- - -")
    print(ourBoard[6] + '|' + ourBoard[7] + '|' + ourBoard[8])

def userInput(symbol, ourBoard):
    while True:
        cell = input('Введите номер ячейки для %s:' % symbol)
        if cell not in '1 2 3 4 5 6 7 8 9':
            print("Вы ввели некорректный номер ячейки")
            continue

        if ourBoard[int(cell) - 1] == 'X':
            print("Ячейка занята!")
            continue

        if ourBoard[int(cell) - 1] == '0':
            print("Ячейка занята!")
            continue
        
        return cell

def checkWinner(symbol, ourBoard):
    # Проверка горизонталей
    if symbol == ourBoard[0] and ourBoard[0] == ourBoard[1] and ourBoard[1] == ourBoard[2]:
        return True

    if symbol == ourBoard[3] and ourBoard[3] == ourBoard[4] and ourBoard[4] == ourBoard[5]:
        return True

    if symbol == ourBoard[6] and ourBoard[6] == ourBoard[7] and ourBoard[7] == ourBoard[8]:
        return True

    # Проверка вертикалей
    if symbol == ourBoard[0] and ourBoard[0] == ourBoard[3] and ourBoard[3] == ourBoard[6]:
        return True

    if symbol == ourBoard[1] and ourBoard[1] == ourBoard[4] and ourBoard[4] == ourBoard[7]:
        return True

    if symbol == ourBoard[2] and ourBoard[2] == ourBoard[5] and ourBoard[5] == ourBoard[8]:
        return True

    # Проверка диагоналей
    if symbol == ourBoard[0] and ourBoard[0] == ourBoard[4] and ourBoard[4] == ourBoard[8]:
        return True

    if symbol == ourBoard[2] and ourBoard[2] == ourBoard[4] and ourBoard[4] == ourBoard[6]:
        return True

    return False

while True:
    printBoard(board)
    cell = userInput('X', board)
    board[int(cell) - 1] = 'X'
    if checkWinner('X', board):
        print("Крестики победили")
        break

    printBoard(board)
    cell = userInput('0', board)
    board[int(cell) - 1] = '0'
    if checkWinner('0', board):
        print("Нолики победили")
        break



























