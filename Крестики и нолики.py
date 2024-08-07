""""Определяем функцию print_board, которая выводит игровое поле"""
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

""""Определяем функцию check_winner, которая проверяет, есть ли победитель."""
def check_winner(board, player):
    # Проверка строк
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Проверка столбцов
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Проверка диагоналей
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

""""Определяем функцию is_full, которая проверяет, заполнено ли поле."""
def is_full(board):
    return all([cell != " " for row in board for cell in row])

""""Основная функция tic_tac_toe содержит основной цикл игры, где игроки по очереди вводят свои ходы."""
def krest_and_nol():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки Кожанный мешок (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца Кожанный мешок (0, 1, 2): "))

        if board[row][col] != " ":
            print("Это место уже занято, открой глаза!")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Мешок {current_player} победил!")
            break

        if is_full(board):
            print_board(board)
            print("Опять 25!")
            break

        current_player = "O" if current_player == "X" else "X"

krest_and_nol()