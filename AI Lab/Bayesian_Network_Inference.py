# ============================================================
# EXPERIMENT 4 - Bayesian Network Inference
# ============================================================
 
print("\n" + "=" * 60)
print("EXPERIMENT 4: Bayesian Network Inference")
print("=" * 60)
 
# Variable Elimination for Inference
 
def normalize(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}
 
def enumeration_ask(X, evidence, bn):
    """
    Simple enumeration-based inference.
    bn: dict with 'variables', 'parents', 'cpt'
    """
    dist = {}
    for xi in [True, False]:
        e_extended = dict(evidence)
        e_extended[X] = xi
        dist[xi] = enumerate_all(bn['variables'], e_extended, bn)
    return normalize(dist)
 
def enumerate_all(variables, evidence, bn):
    if not variables:
        return 1.0
    Y = variables[0]
    rest = variables[1:]
    if Y in evidence:
        return p_of(Y, evidence[Y], evidence, bn) * enumerate_all(rest, evidence, bn)
    else:
        total = 0
        for y in [True, False]:
            e_extended = dict(evidence)
            e_extended[Y] = y
            total += p_of(Y, y, e_extended, bn) * enumerate_all(rest, e_extended, bn)
        return total
 
def p_of(var, val, evidence, bn):
    parents = bn['parents'][var]
    if not parents:
        return bn['cpt'][var][val]
    parent_vals = tuple(evidence[p] for p in parents)
    return bn['cpt'][var][(parent_vals, val)]
 
# Define the Bayesian Network
bn = {
    'variables': ['Rain', 'Sprinkler', 'WetGrass'],
    'parents': {
        'Rain': [],
        'Sprinkler': ['Rain'],
        'WetGrass': ['Rain', 'Sprinkler'],
    },
    'cpt': {
        'Rain': {True: 0.2, False: 0.8},
        'Sprinkler': {
            ((True,),  True):  0.01,
            ((True,),  False): 0.99,
            ((False,), True):  0.40,
            ((False,), False): 0.60,
        },
        'WetGrass': {
            ((True,  True),  True):  0.99,
            ((True,  True),  False): 0.01,
            ((True,  False), True):  0.80,
            ((True,  False), False): 0.20,
            ((False, True),  True):  0.90,
            ((False, True),  False): 0.10,
            ((False, False), True):  0.00,
            ((False, False), False): 1.00,
        }
    }
}
 
print("\nInference: P(Rain | WetGrass=True)")
result_inf = enumeration_ask('Rain', {'WetGrass': True}, bn)
print(f"  P(Rain=True  | WetGrass=True) = {result_inf[True]:.4f}")
print(f"  P(Rain=False | WetGrass=True) = {result_inf[False]:.4f}")
 
print("\nInference: P(Sprinkler | WetGrass=True)")
result_spr = enumeration_ask('Sprinkler', {'WetGrass': True}, bn)
print(f"  P(Sprinkler=True  | WetGrass=True) = {result_spr[True]:.4f}")
print(f"  P(Sprinkler=False | WetGrass=True) = {result_spr[False]:.4f}")
 