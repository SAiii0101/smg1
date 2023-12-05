def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_n_queens_util(board, col, n):
    if col == n:
        # All queens are placed successfully, print the solution
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen and check the next column
            board[i][col] = 1

            # Recur to place the rest of the queens
            res = solve_n_queens_util(board, col + 1, n) or res

            # If placing queen in the current position doesn't lead to a solution
            # then remove the queen from the current position (backtrack)
            board[i][col] = 0

    return res

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
    else:
        print("All solutions printed above.")

if __name__ == "__main__":
    n = 8  # Change this to the desired number of queens
    solve_n_queens(n)
