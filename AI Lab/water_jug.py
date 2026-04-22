# ── B) Water Jug Problem ─────────────────────────────────────
print("\n--- B) Water Jug Problem ---")
from math import gcd
 
def pour(from_cap, to_cap, d):
    frm = from_cap
    to = 0
    step = 1
    while frm != d and to != d:
        temp = min(frm, to_cap - to)
        to += temp
        frm -= temp
        step += 1
        if frm == d or to == d:
            break
        if frm == 0:
            frm = from_cap
            step += 1
        if to == to_cap:
            to = 0
            step += 1
    return step
 
def min_steps(m, n, d):
    if m > n:
        m, n = n, m
    if d > n:
        return -1
    if d % gcd(n, m) != 0:
        return -1
    return min(pour(n, m, d), pour(m, n, d))
 
n_jug, m_jug, d_jug = 3, 5, 4
print(f"Jugs: {m_jug}L and {n_jug}L, Target: {d_jug}L")
print(f"Minimum number of steps required is: {min_steps(m_jug, n_jug, d_jug)}")
 