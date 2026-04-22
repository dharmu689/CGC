# ── C) 8-Puzzle / 3x3 Puzzle (A* / Best-First) ──────────────
print("\n--- C) 8-Puzzle Solver (A* Search) ---")
import heapq
import copy
 
N = 3
 
def calculate_cost(state, goal):
    cost = 0
    for i in range(N):
        for j in range(N):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                cost += 1
    return cost
 
def find_blank(state):
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                return i, j
 
def solve_puzzle(initial, goal):
    row_moves = [1, 0, -1, 0]
    col_moves = [0, -1, 0, 1]
 
    start_cost = calculate_cost(initial, goal)
    # (f, level, state, path)
    heap = [(start_cost, 0, initial, [initial])]
    visited = set()
 
    while heap:
        f, level, state, path = heapq.heappop(heap)
        state_key = str(state)
        if state_key in visited:
            continue
        visited.add(state_key)
 
        if calculate_cost(state, goal) == 0:
            return path
 
        x, y = find_blank(state)
        for i in range(4):
            nx, ny = x + row_moves[i], y + col_moves[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_state = copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_cost = calculate_cost(new_state, goal)
                heapq.heappush(heap, (new_cost + level + 1, level + 1, new_state, path + [new_state]))
    return None
 
initial_puzzle = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
goal_puzzle    = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
 
print("Initial State:")
for row in initial_puzzle:
    print(row)
print("Goal State:")
for row in goal_puzzle:
    print(row)
 
solution = solve_puzzle(initial_puzzle, goal_puzzle)
if solution:
    print(f"\nSolution found in {len(solution)-1} moves:")
    for step in solution:
        for row in step:
            print(row)
        print()