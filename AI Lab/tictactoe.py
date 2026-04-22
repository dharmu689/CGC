# ── D) Minimax Algorithm (Tic-Tac-Toe) ──────────────────────
print("\n--- D) Minimax Algorithm (Tic-Tac-Toe) ---")
 
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
 
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
 
def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
 
def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0
 
    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, False))
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, True))
                    board[i][j] = ' '
        return best
 
def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move
 
def play_tictactoe():
    board = [[' '] * 3 for _ in range(3)]
    print("Tic-Tac-Toe: Computer (O) vs Human (X)")
    print_board(board)
 
    for turn in range(9):
        if turn % 2 == 0:  # Computer's turn
            row, col = best_move(board)
            board[row][col] = 'O'
            print(f"Computer placed O at ({row}, {col})")
        else:              # Human's turn (auto for demo)
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        print(f"Human placed X at ({i}, {j})")
                        break
                else:
                    continue
                break
        print_board(board)
        if check_winner(board, 'O'):
            print("COMPUTER has won!")
            return
        if check_winner(board, 'X'):
            print("HUMAN has won!")
            return
    print("It's a draw!")
 
play_tictactoe()