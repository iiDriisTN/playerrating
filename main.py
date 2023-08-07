T = float(input("Give me touches: "))
P = float(input("Give me penalties: "))
A = float(input("Give me assists: "))
S = float(input("Give me scores: "))
PA = float(input("Give me passes: "))
delta_T = float(input("Give me play time: "))
R = (0.1 * T - 0.5 * P + 0.8 * A + 1.8 * S + 0.3 * PA) * 140 / delta_T
print("Player rating:", R)
