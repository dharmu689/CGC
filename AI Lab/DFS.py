# ============================================================
# EXPERIMENT 1 - Uninformed & Informed Search
# ============================================================
 
print("=" * 60)
print("EXPERIMENT 1: Uninformed & Informed Search")
print("=" * 60)
 
# ── A) Breadth-First Search (BFS) ───────────────────────────
print("\n--- A) Breadth-First Search (BFS) ---")
 
graph_bfs = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
 
def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()
 
print("Following is the Breadth-First Search:")
bfs(graph_bfs, '5')
 