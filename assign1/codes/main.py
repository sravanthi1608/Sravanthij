import numpy as np
import matplotlib.pyplot as plt

# Define coordinates of points
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])
G = np.array([-2, 0])
D = (B + C) / 2
E = (C + A) / 2
F = (A + B) / 2
#print("Solution:", solution)
#G = (A + B + C) / 3
# Calculate vectors and lengths
BG = G - B
GE = E - G
CG = G - C
GF = F - G
AG = G - A
GD = D - G
# Calculate ratios
ratio_BG_GE = np.linalg.norm(BG) / np.linalg.norm(GE)
ratio_CG_GF = np.linalg.norm(CG) / np.linalg.norm(GF)
ratio_AG_GD = np.linalg.norm(AG) / np.linalg.norm(GD)

print("Ratio BG/GE:", ratio_BG_GE)
print("Ratio CG/GF:", ratio_CG_GF)
print("Ratio AG/GD:", ratio_AG_GD)
print("Hence BG/GE=CG/GF=AG/GD=2 is verified.")
