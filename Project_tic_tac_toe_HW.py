# Добавить возможность ввода Х на англ и рус и О буквой и цифрой v
# добавить право выбора чем ходить v
# добавить кто первый ходит (первый всегда крестик) v
# добавить ничью v
# добавить зачеркивание победившей строки (по возможности) x
# добавить счетчик побед и кто ходит первым в следующей игре x

import random


# 3. Создайте функцию "draw_board", которая будет рисовать игровое поле в консоли.
# Она должна принимать список из девяти элементов, представляющих игровое поле:
def draw_board(board):
    for i in range(1, 10, 3):  # создаем игровое поле по 3 элемента в строке
        print('|', board[i], board[i + 1], board[i + 2], '|')
        # print('-------------')    # если хотим добавить горизонтальный разделитель


# check
# board = list(range(10))
# draw_board(board)


# 4. Создайте функцию "get_player_move", которая будет запрашивать у игрока ход
# и проверять его на корректность. Она должна принимать список из девяти элементов,
# представляющих игровое поле, и символ, которым играет игрок (X или O):

def get_player_move(board,
                    symbol):  # запрашиваем номер ячейки куда хочет походить клиент (пока не спрашиваем чем он ходит)
    # и возвращаем его (y) для предыдущей функции
    y = input(f"Введите номер ячейки от 1 до 9, в которую хотите вставить свой {symbol}: ")
    # Нужно проверить, что клиент ввел цифру от 1 до 9 (не вышел за рамки списка)
    # и ввел корректный символ. После чего проверяем, что ячейка не занята. Если занята, то нужно проверить все сначала
    while y not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or board[int(y)] in "XO":
        if y not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            y = input(f"Введите корректный номер ячейки цифрой от 1 до 9: \n")
        if y in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and board[int(y)] in "XO":
            y = input(f" ячейка уже занята, выберите другую свободную от 1 до 9: \n")

    return int(y)


# check
# board = [str(i) for i in range(10)]
# board[5] = "x"
# print(board)
# draw_board(board)
#
# print(get_player_move(board, "X"))
# draw_board(board)

# 5. Создайте функцию "get_computer_move", которая будет генерировать случайный
# ход компьютера. Она должна принимать список из девяти элементов, представляющих
# игровое поле, и символ, которым играет компьютер (X или O):

def get_computer_move(board, symbol):  # нужно проверить свободные ячейки и сделать рандомный ход

    free_i = []
    for i in range(1, len(board)):  # collect free cells for random
        if board[i] not in "XO":
            free_i.append(i)
        # print(free_i) #check what cells are free
    return random.choice(free_i)  # выбирает из доступных ячеек рандомно одну


# check
# board = [str(i) for i in range(10)]
# board[5] = "X"
# board[2] = "о"
# print(board)
# draw_board(board)
# print(get_computer_move(board, "0"))

# 6. Создайте функцию "check_win", которая будет проверять, есть ли победитель
# в игре. Она должна принимать список из девяти элементов, представляющих
# игровое поле, и символ, которым играет игрок (X или O):

def check_win(board, symbol):  # проверяем выигрышные комбинации, победил ли кто
    # и выводим рез-т в виде имени победителя и результата

    for i1 in range(1, 10, 3):  # проверка горизонтали
        if board[i1] == board[i1 + 1] == board[i1 + 2]:
            print(f'победитель {board[i1]} по горизонтали!')
            return True
    for i2 in range(1, 4):  # проверка вертикали
        if board[i2] == board[i2 + 3] == board[i2 + 6]:
            print(f'победитель {board[i2]} по вертикали!')
            return True
    if board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:  # проверка диагонали
        print(f'победитель {board[5]} по диагонали!')
        return True
    for i3 in range(10):  # добавляем проверку на ничью
        if board[i3] not in ('X', 'O', '0'):
            return False
    print(f'Игра завершилась вничью!')
    return True


# check
# board = [str(i) for i in range(10)]
# board[7] = "O"
# board[8] = "X"
# board[9] = "O"
# board[1] = "O"
# board[2] = "O"
# board[3] = "X"
# board[4] = "X"
# board[5] = "X"
# board[6] = "O"
# print(board)
# draw_board(board)
#
# print(check_win(board, "0"))

# 7. Создайте функцию "main", которая будет запускать игру.
# Она должна создавать список из девяти элементов, представляющих игровое поле,
# и запускать цикл, в котором игроки будут делать ходы до тех пор, пока не будет
# победитель или не закончится свободное место на игровом поле:
#
def main():
    board = [str(i) for i in range(10)]  # задаем игровое поле

    PS = input(
        f"Введите каким символом будете играть: Х или О: ").upper()  # выбор, каким символом хочет играть пользователь.
    # Он может выбрать как русские символы большие и маленькие так, и англ. плюс ноль.
    while PS not in "ХXOО0":
        PS = input(f"Введите корректный символ: Х или О: \n").upper()
    dict_for_replace = {"Х": "X", "X": "X", "0": "O", "O": "O", "О": "O"}  # замена некорректных символов
    player_symb = dict_for_replace[PS]

    if player_symb == "X":
        computer_symb = "O"
    else:
        computer_symb = "X"
    print("Игра начинается. Перед вами игровая доска:")
    draw_board(board)

    while True:
        if computer_symb == "X":  # согласно правилам игры, кто ходит Х, тот ходит первым
            computer_i = get_computer_move(board, computer_symb)  # выбор и заполнение ячейки компьютером
            board[computer_i] = computer_symb
            print(f"Доска после хода компьютера символом {computer_symb}")
            draw_board(board)
            if check_win(board, computer_symb):  # проверка на победителя
                break
            player_i = get_player_move(board, player_symb)  # ход и заполнение ячейки игроком
            board[player_i] = player_symb
            print(f"Доска после вашего хода {player_symb}")
            draw_board(board)
            if check_win(board, player_symb):     # проверка на победителя
                break
        else:   # этот блок всё то же самое, но если первый ходит игрок
            player_i = get_player_move(board, player_symb)
            board[player_i] = player_symb
            print(f"Доска после вашего хода {player_symb}")
            draw_board(board)
            if check_win(board, player_symb):
                break
            computer_i = get_computer_move(board, computer_symb)
            board[computer_i] = computer_symb
            print(f"Доска после хода компьютера символом {computer_symb}")
            draw_board(board)
            if check_win(board, computer_symb):
                break


main()
