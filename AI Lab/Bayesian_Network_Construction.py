# ============================================================
# EXPERIMENT 3 - Bayesian Network Construction
# ============================================================
 
print("\n" + "=" * 60)
print("EXPERIMENT 3: Bayesian Network Construction from Data")
print("=" * 60)
 
# Manual Bayesian Network using conditional probability tables (CPTs)
 
# Example: Wet Grass Problem
# Variables: Rain (R), Sprinkler (S), WetGrass (W)
# P(R), P(S|R), P(W|R,S)
 
P_Rain = {True: 0.2, False: 0.8}
 
P_Sprinkler_given_Rain = {
    True:  {True: 0.01, False: 0.99},
    False: {True: 0.40, False: 0.60},
}
 
P_WetGrass_given_Rain_Sprinkler = {
    (True,  True):  {True: 0.99, False: 0.01},
    (True,  False): {True: 0.80, False: 0.20},
    (False, True):  {True: 0.90, False: 0.10},
    (False, False): {True: 0.00, False: 1.00},
}
 
def bayesian_network_joint(rain, sprinkler, wet_grass):
    p_r  = P_Rain[rain]
    p_s  = P_Sprinkler_given_Rain[rain][sprinkler]
    p_w  = P_WetGrass_given_Rain_Sprinkler[(rain, sprinkler)][wet_grass]
    return p_r * p_s * p_w
 
print("\nBayesian Network: Wet Grass Problem")
print(f"{'Rain':<8} {'Sprinkler':<12} {'WetGrass':<12} {'Joint P':<12}")
print("-" * 48)
for r in [True, False]:
    for s in [True, False]:
        for w in [True, False]:
            jp = bayesian_network_joint(r, s, w)
            print(f"{str(r):<8} {str(s):<12} {str(w):<12} {jp:.6f}")
 
# Calculate P(Rain | WetGrass = True) using enumeration
def p_rain_given_wetgrass(wet_grass=True):
    p_rain_and_wet = 0
    p_not_rain_and_wet = 0
    for s in [True, False]:
        p_rain_and_wet    += bayesian_network_joint(True,  s, wet_grass)
        p_not_rain_and_wet += bayesian_network_joint(False, s, wet_grass)
    total = p_rain_and_wet + p_not_rain_and_wet
    return p_rain_and_wet / total
 
result = p_rain_given_wetgrass(True)
print(f"\nP(Rain=True | WetGrass=True) = {result:.4f}")
print(f"P(Rain=False | WetGrass=True) = {1-result:.4f}")
