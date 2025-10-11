"""
yield_distribution_plot.py — ICECIE 2025 Supplementary Simulation
Plots η_fusion yield distribution for the caesium-free magnetic filter model.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fusion_efficiency_map.csv", delimiter=",")

plt.figure(figsize=(6,4))
plt.imshow(data, extent=[5,50,0.2,5], origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label="η_fusion (dimensionless)")
plt.xlabel("Input Power P_input (kW)")
plt.ylabel("Magnetic Field B (T)")
plt.title("Fusion Efficiency Scaling Map — Eq. (1)")
plt.tight_layout()
plt.savefig("fusion_efficiency_map.png", dpi=300)
plt.show()
