"""
fusion_filter_sim.py — ICECIE 2025 Supplementary Simulation
Author: Paul D. Markov, Harmony Research Initiative
Description: Simulates caesium-free H⁻ source efficiency using Eq. (1)
η_fusion = C * (n_Hm / n_e) * (B / P_input)
"""

import numpy as np

# Constants (dimensionless or SI)
C = 0.87  # scaling coefficient
B = np.linspace(0.2, 5.0, 50)       # magnetic field [T]
P_input = np.linspace(5, 50, 50)    # input power [kW]
n_Hm_ne = 0.1                       # H⁻ fraction

# Compute efficiency η_fusion
eta_fusion = C * n_Hm_ne * (B[:, None] / P_input[None, :])

# Display results
print("Fusion efficiency map (η_fusion) across B and P_input:")
print(eta_fusion)

# Save to file
np.savetxt("fusion_efficiency_map.csv", eta_fusion, delimiter=",")
print("\nSaved to fusion_efficiency_map.csv")
