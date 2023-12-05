import heapq
import copy

class PuzzleState:
    def __init__(self, board, parent=None, move=None, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        h = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_row, target_col = divmod(self.board[i][j] - 1, 3)
                    h += abs(i - target_row) + abs(j - target_col)
        return h

def get_blank_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    blank_row, blank_col = get_blank_position(state.board)

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = blank_row + move[0], blank_col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_board = copy.deepcopy(state.board)
            new_board[blank_row][blank_col], new_board[new_row][new_col] = (
                new_board[new_row][new_col],
                new_board[blank_row][blank_col],
            )
            neighbors.append(
                PuzzleState(new_board, parent=state, move=(new_row, new_col), cost=state.cost + 1)
            )

    return neighbors

def a_star(initial_state):
    heap = [initial_state]
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)

        if current_state.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return current_state

        if current_state not in visited:
            visited.add(current_state)

            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    heapq.heappush(heap, neighbor)

    return None

def print_solution(solution):
    moves = []
    while solution:
        moves.append(solution.move)
        solution = solution.parent

    moves.reverse()
    for move in moves:
        print(f"Move {move}:")

if __name__ == "__main__":
    # Example initial state (change as needed)
    initial_board = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    initial_state = PuzzleState(initial_board)

    solution = a_star(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
