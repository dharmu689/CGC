# ── C) A* Search (Informed Search) ──────────────────────────
print("\n--- C) A* Search (Informed Search) ---")
import heapq
 
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
 
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
 
    while open_set:
        f, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue            
        visited.add(current)
        if current == goal:
            return path, cost
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    new_cost = cost + 1
                    heapq.heappush(open_set,
                        (new_cost + heuristic(neighbor, goal),
                         new_cost, neighbor, path + [neighbor]))
    return None, -1
 
# 0 = free, 1 = wall
grid_astar = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
start_a, goal_a = (0, 0), (4, 4)
path_a, cost_a = astar(grid_astar, start_a, goal_a)
print(f"A* Path from {start_a} to {goal_a}: {path_a}")
print(f"Total Cost: {cost_a}")