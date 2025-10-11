# Fusion Resonance — Caesium-Free NBI (IEEE ICECIE 2025)

**Author:** Paul D. Markov  
**Affiliation:** Harmony Research Initiative, Australia  
**Conference:** IEEE 7th International Conference on Electrical, Control and Instrumentation Engineering (ICECIE 2025)

---

## Overview
This repository contains the simulation code, figures, and data that support the IEEE ICECIE 2025 paper  
**“Enhancing Fusion Neutral Beam Injection Efficiency with a Caesium-Free Magnetic Filter.”**  
The project demonstrates a 14–16 % efficiency improvement in neutral beam injection (NBI) through a magnetically confined, caesium-free hydrogen plasma source.

---

## Repository Contents
- `simulation/fusion_filter_sim.py` — Main Python script computing η_fusion (Eq. 1)  
- `simulation/yield_distribution_plot.py` — Generates Fig. 2 (yield distribution)  
- `simulation/parameters.json` — Simulation parameters (magnetic field, pressure, RF power)  
- `figures/` — High-resolution figures and Table I data  
- `docs/Markov_ICECIE2025_AppendixA_SimCode.pdf` — Supplementary appendix

---

## Environment
- Python ≥ 3.10  
- NumPy, Matplotlib, SciPy  

```bash
pip install numpy matplotlib scipy
python simulation/fusion_filter_sim.py
python simulation/yield_distribution_plot.py
