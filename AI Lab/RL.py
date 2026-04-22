
# ============================================================
# EXPERIMENT 6 - Reinforcement Learning (Q-Learning Grid World)
# ============================================================
 
print("\n" + "=" * 60)
print("EXPERIMENT 6: Reinforcement Learning in Grid World")
print("=" * 60)
 
import numpy as np
import random
 
# ── Q-Learning ───────────────────────────────────────────────
print("\n--- Q-Learning ---")
 
ROWS, COLS = 4, 4
ACTIONS = 4          # 0=Up, 1=Down, 2=Left, 3=Right
ALPHA   = 0.1        # Learning rate
GAMMA_Q = 0.9        # Discount factor
EPSILON = 0.2        # Exploration rate
EPISODES = 1000
 
# Same grid as Exp 5
q_grid = [
    [0,  0,  0,  0],
    [0, -1,  0, -1],
    [0,  0,  0, -1],
    [-1, 0,  0,  1],
]
 
def is_terminal_q(r, c):
    return q_grid[r][c] == 1 or q_grid[r][c] == -1
 
def step(r, c, action):
    if action == 0:   nr, nc = r-1, c
    elif action == 1: nr, nc = r+1, c
    elif action == 2: nr, nc = r,   c-1
    else:             nr, nc = r,   c+1
 
    if 0 <= nr < ROWS and 0 <= nc < COLS:
        reward = q_grid[nr][nc]
        done   = is_terminal_q(nr, nc)
        return nr, nc, reward, done
    return r, c, -0.01, False  # Bumped into wall
 
Q = np.zeros((ROWS, COLS, ACTIONS))
rewards_per_episode = []
 
for episode in range(EPISODES):
    # Start at top-left
    r, c = 0, 0
    total_reward = 0
    steps = 0
 
    while True:
        # Epsilon-greedy action selection
        if random.random() < EPSILON:
            action = random.randint(0, ACTIONS - 1)
        else:
            action = np.argmax(Q[r, c])
 
        nr, nc, reward, done = step(r, c, action)
        total_reward += reward
 
        # Q-update
        best_next = np.max(Q[nr, nc])
        Q[r, c, action] += ALPHA * (reward + GAMMA_Q * best_next - Q[r, c, action])
 
        r, c = nr, nc
        steps += 1
        if done or steps > 100:
            break
 
    rewards_per_episode.append(total_reward)
 
print(f"Q-Learning trained for {EPISODES} episodes")
print(f"Average reward (last 100 episodes): {np.mean(rewards_per_episode[-100:]):.3f}")
 
# Extract learned policy
action_sym = ['↑', '↓', '←', '→']
print("\nLearned Policy (Q-Learning):")
for r in range(ROWS):
    row_str = "  "
    for c in range(COLS):
        if is_terminal_q(r, c):
            row_str += " T  "
        else:
            row_str += f" {action_sym[np.argmax(Q[r,c])]}  "
    print(row_str)
 
print("\nQ-Values (max per state):")
print(np.round(np.max(Q, axis=2), 3))
 
 
# ── SARSA ────────────────────────────────────────────────────
print("\n--- SARSA ---")
 
Q_sarsa = np.zeros((ROWS, COLS, ACTIONS))
rewards_sarsa = []
 
def epsilon_greedy(Q_table, r, c, eps):
    if random.random() < eps:
        return random.randint(0, ACTIONS - 1)
    return int(np.argmax(Q_table[r, c]))
 
for episode in range(EPISODES):
    r, c = 0, 0
    action = epsilon_greedy(Q_sarsa, r, c, EPSILON)
    total_reward = 0
    steps = 0
 
    while True:
        nr, nc, reward, done = step(r, c, action)
        next_action = epsilon_greedy(Q_sarsa, nr, nc, EPSILON)
        total_reward += reward
 
        # SARSA update
        Q_sarsa[r, c, action] += ALPHA * (
            reward + GAMMA_Q * Q_sarsa[nr, nc, next_action] - Q_sarsa[r, c, action]
        )
 
        r, c, action = nr, nc, next_action
        steps += 1
        if done or steps > 100:
            break
 
    rewards_sarsa.append(total_reward)
 
print(f"SARSA trained for {EPISODES} episodes")
print(f"Average reward (last 100 episodes): {np.mean(rewards_sarsa[-100:]):.3f}")
 
print("\nLearned Policy (SARSA):")
for r in range(ROWS):
    row_str = "  "
    for c in range(COLS):
        if is_terminal_q(r, c):
            row_str += " T  "
        else:
            row_str += f" {action_sym[np.argmax(Q_sarsa[r,c])]}  "
    print(row_str)
 
 
# ── Vertex Cover (Graph Problem) ─────────────────────────────
print("\n--- Vertex Cover (Greedy Approximation) ---")
 
def vertex_cover(n, edges):
    visited = [False] * (n + 1)
    cover = []
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
 
    for u in range(1, n + 1):
        if not visited[u]:
            for v in adj[u]:
                if not visited[v]:
                    visited[u] = True
                    visited[v] = True
                    cover.append(u)
                    cover.append(v)
                    break
    return sorted(cover)
 
edges_vc = [(1, 2), (1, 3), (4, 3), (4, 2)]
n_vc = 4
cover = vertex_cover(n_vc, edges_vc)
print(f"Vertices: {n_vc}, Edges: {edges_vc}")
print(f"Vertex Cover: {cover}")
 
 
# ============================================================
print("\n" + "=" * 60)
print("All 6 Experiments Completed Successfully!")
print("=" * 60)
 