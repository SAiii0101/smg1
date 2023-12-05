import random

def generate_random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_attacks(board):
    n = len(board)
    attacks = 0

    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1

    return attacks

def hill_climbing(n):
    current_board = generate_random_board(n)
    current_attacks = calculate_attacks(current_board)

    while current_attacks > 0:
        neighbor_boards = []
        for col in range(n):
            for row in range(n):
                if current_board[col] != row:
                    neighbor_board = list(current_board)
                    neighbor_board[col] = row
                    neighbor_boards.append(neighbor_board)

        best_neighbor = min(neighbor_boards, key=calculate_attacks)
        best_neighbor_attacks = calculate_attacks(best_neighbor)

        if best_neighbor_attacks >= current_attacks:
            break  # Stuck in a local minimum, terminate

        current_board = best_neighbor
        current_attacks = best_neighbor_attacks

    return current_board

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ["Q" if j == board[i] else "." for j in range(n)]
        print(" ".join(row))
    print()

# Example usage for 8-Queens problem
n = 8
solution = hill_climbing(n)

if solution:
    print("Solution:")
    print_board(solution)
else:
    print("No solution found.")
