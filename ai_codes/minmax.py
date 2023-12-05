import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def evaluate(board):
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, is_maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if is_maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Cell already occupied. Try again.")
            continue

        # Check if player wins
        if is_winner(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")
            game_over = True
            break

        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
            break

        print_board(board)

        # AI's move
        print("AI is thinking...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'X'

        # Check if AI wins
        if is_winner(board, 'X'):
            print_board(board)
            print("AI wins! Better luck next time.")
            game_over = True
            break

        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
            break

if __name__ == "__main__":
    play_tic_tac_toe()
