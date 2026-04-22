# ============================================================
# EXPERIMENT 5 - Value and Policy Iteration (MDP Grid World)
# ============================================================
 
print("\n" + "=" * 60)
print("EXPERIMENT 5: Value and Policy Iteration in Grid Network")
print("=" * 60)
 
import numpy as np
 
# 4x4 Grid World MDP
# S = Start, G = Goal (+1 reward), H = Hole (-1 reward), . = Empty
# Actions: 0=Up, 1=Down, 2=Left, 3=Right
 
GRID_ROWS = 4
GRID_COLS = 4
NUM_STATES = GRID_ROWS * GRID_COLS
NUM_ACTIONS = 4
GAMMA = 0.9       # Discount factor
THETA = 1e-6      # Convergence threshold
 
# Grid layout (0=empty, 1=goal, -1=hole)
grid = [
    [0,  0,  0,  0],
    [0, -1,  0, -1],
    [0,  0,  0, -1],
    [-1, 0,  0,  1],
]
 
def state_to_coord(s):
    return s // GRID_COLS, s % GRID_COLS
 
def coord_to_state(r, c):
    return r * GRID_COLS + c
 
def is_terminal(s):
    r, c = state_to_coord(s)
    return grid[r][c] == 1 or grid[r][c] == -1
 
def get_reward(s):
    r, c = state_to_coord(s)
    return grid[r][c]
 
# Transition: deterministic (stochastic noise = 0)
def get_next_state(s, a):
    if is_terminal(s):
        return s
    r, c = state_to_coord(s)
    if a == 0: nr, nc = r-1, c      # Up
    elif a == 1: nr, nc = r+1, c    # Down
    elif a == 2: nr, nc = r,   c-1  # Left
    else:        nr, nc = r,   c+1  # Right
    if 0 <= nr < GRID_ROWS and 0 <= nc < GRID_COLS:
        return coord_to_state(nr, nc)
    return s  # Stay if out of bounds
 
# ── Value Iteration ──────────────────────────────────────────
print("\n--- Value Iteration ---")
 
V = np.zeros(NUM_STATES)
iteration = 0
 
while True:
    delta = 0
    new_V = np.copy(V)
    for s in range(NUM_STATES):
        if is_terminal(s):
            new_V[s] = get_reward(s)
            continue
        action_values = []
        for a in range(NUM_ACTIONS):
            ns = get_next_state(s, a)
            action_values.append(get_reward(ns) + GAMMA * V[ns])
        new_V[s] = max(action_values)
        delta = max(delta, abs(new_V[s] - V[s]))
    V = new_V
    iteration += 1
    if delta < THETA:
        break
 
print(f"Value Iteration converged in {iteration} iterations")
print("\nOptimal Value Function (V*):")
print(np.round(V.reshape(GRID_ROWS, GRID_COLS), 3))
 
# Extract policy from V
action_symbols = ['↑', '↓', '←', '→']
policy_vi = []
for s in range(NUM_STATES):
    if is_terminal(s):
        policy_vi.append('T')
    else:
        best_a = max(range(NUM_ACTIONS),
                     key=lambda a: get_reward(get_next_state(s,a)) + GAMMA * V[get_next_state(s,a)])
        policy_vi.append(action_symbols[best_a])
 
print("\nOptimal Policy (Value Iteration):")
for r in range(GRID_ROWS):
    print("  " + "  ".join(policy_vi[r*GRID_COLS:(r+1)*GRID_COLS]))
 
# ── Policy Iteration ─────────────────────────────────────────
print("\n--- Policy Iteration ---")
 
policy = np.zeros(NUM_STATES, dtype=int)  # Start with all "Up"
V_pi = np.zeros(NUM_STATES)
pi_iteration = 0
 
while True:
    # Policy Evaluation
    while True:
        delta = 0
        for s in range(NUM_STATES):
            if is_terminal(s):
                V_pi[s] = get_reward(s)
                continue
            a = policy[s]
            ns = get_next_state(s, a)
            v_new = get_reward(ns) + GAMMA * V_pi[ns]
            delta = max(delta, abs(v_new - V_pi[s]))
            V_pi[s] = v_new
        if delta < THETA:
            break
 
    # Policy Improvement
    policy_stable = True
    for s in range(NUM_STATES):
        if is_terminal(s):
            continue
        old_action = policy[s]
        best_a = max(range(NUM_ACTIONS),
                     key=lambda a: get_reward(get_next_state(s,a)) + GAMMA * V_pi[get_next_state(s,a)])
        policy[s] = best_a
        if old_action != best_a:
            policy_stable = False
    pi_iteration += 1
    if policy_stable:
        break
 
print(f"Policy Iteration converged in {pi_iteration} iterations")
print("\nOptimal Value Function (Policy Iteration):")
print(np.round(V_pi.reshape(GRID_ROWS, GRID_COLS), 3))
 
policy_pi = [action_symbols[policy[s]] if not is_terminal(s) else 'T'
             for s in range(NUM_STATES)]
print("\nOptimal Policy (Policy Iteration):")
for r in range(GRID_ROWS):
    print("  " + "  ".join(policy_pi[r*GRID_COLS:(r+1)*GRID_COLS]))
 
 
# ── Forward Chaining (Knowledge Base) ───────────────────────
print("\n--- Forward Chaining Demo ---")
 
database  = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase  = ["Frog", "Canary", "Green", "Yellow"]
 
def forward_chaining_demo(x, k):
    print(f"\nSelected: X = {database[x-1]}")
    if x in [1, 2]:
        print("Chance Of Frog")
    elif x in [3, 4]:
        print("Chance of Canary")
    else:
        print("Invalid Option Selected")
        return
 
    color = "Green" if k == 1 else "Yellow"
    print(f"Color selected: {color}")
 
    if k == 1 and x in [1, 2]:
        print(f"Yes it is {knowbase[0]} And Color Is {knowbase[2]}")
    elif k == 2 and x in [3, 4]:
        print(f"Yes it is {knowbase[1]} And Color Is {knowbase[3]}")
    else:
        print("Invalid Knowledge Database")
 
forward_chaining_demo(x=1, k=1)
forward_chaining_demo(x=3, k=2)