# Bayesian Network

## Overview
This project applies **Bayesian inference** to locate hidden gems on a grid from distance observations.  
We use **enumeration-based inference** (exact, model-driven) to update the belief distribution after each observation and visualize how beliefs converge toward the true gem positions.

---

## Methodology
- **Grid world:** discretized cells where each cell can contain a gem.
- **Observations:** distance-based readings (vectors) relative to hypothesized gem positions.
- **Likelihood:** decreases exponentially with mismatch between prediction and observation (e.g., \(2^{-d}\), where \(d\) is a distance measure).
- **Inference (enumeration):**
  - Enumerate candidate configurations.
  - Compute likelihood per configuration.
  - Aggregate to cell-wise beliefs and **normalize** to obtain a probability distribution.

---

## Results
- Beliefs are initially spread (near-uniform) and **concentrate** around the plausible gem locations as new observations arrive.
- Over successive updates, the belief map **converges** toward the true positions (clear peaks).
- Exact enumeration gives interpretable results at small/medium scales; for larger grids, approximate methods (e.g., **particle filtering**) are promising extensions.
  
<img width="552" height="63" alt="Screenshot 2024-11-10 at 23 49 28" src="https://github.com/user-attachments/assets/aa52662c-6cf1-41f3-bc79-da238470ce93" />

## Files
- [main.py](main.py) — Entry point
- [bayesian_network.py](bayesian_network.py) — Bayesian network model and enumeration-based inference logic.
- [grid.py](grid.py) — Grid/world representation and utilities
- [bayesian_network_report.pdf](bayesian_network_report.pdf) — Project report.
