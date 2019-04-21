def draw_board(b):
    print("-" * 13)
    for i in range(3):
        print("|", b[0+i*3], "|", b[1+i*3], "|", b[2+i*3], "|")
        print("-" * 13)


player_answer = 0
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_taken = 'X'
move = 1


def player_input(p_t, m):
    result = 'game'
    while not result == 'Победил':
        if m % 2 == 0:
            p_t = 'X'
        else:
            p_t = 'O'
        p_a = input('Куда поставить' + p_t + '?')
        if p_a in number:
            p_a = int(p_a)
            if p_a >= 1 and p_a <= 9:
                if board[p_a - 1] != 'X' and board[p_a - 1] != 'O':
                    board[p_a - 1] = p_t
                    print(draw_board(board))
                    sum = 0
                    for j in number:
                        if int(j) not in board:
                            sum += 1
                    if sum == 9:
                        result = 'Ничья'
                        print('Ничья')
                        break
                    if board[0] == board[1] == board[2] \
                            or board[3] == board[4] == board[5] \
                            or board[6] == board[7] == board[8] \
                            or board[0] == board[3] == board[6] \
                            or board[1] == board[4] == board[7] \
                            or board[2] == board[5] == board[8] \
                            or board[0] == board[4] == board[8] \
                            or board[2] == board[4] == board[6]:
                        result = 'Победил'
                        print(result, p_t)
                    else:
                        result = 'no'
                        m += 1
                else:
                    print('Эта клетка занята')
            else:
                print('Вы ввели неверное число')
        else:
            print('Вы ввели неверное число')


draw_board(board)
