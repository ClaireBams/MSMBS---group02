# Epidemiological Model Assignment — Parameter Exploration

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 02

---

## 1. Repository overview
- `analysis.ipynb` — main notebook containing all required sections (Setup, Part 1–3, Conclusions)
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, scipy, seaborn)
- `README.md` — this file

**How to run**: `pip install -r requirements.txt` then open and run `analysis.ipynb` top to bottom

---

## 2. Part 1 — Parameter analysis function
**Function**: `analyze_recovery_rates(beta, mu, N, I0, simulation_days)`
- Brief description of your approach

The function runs the SIRD model for five recovery rates (γ = 0.05, 0.10, 0.15, 0.20, 0.25). For each value, it calculates the basic reproduction number, peak number of infected individuals, peak day, total deaths, and epidemic duration. It also plots the epidemic curves for comparison.

- Output DataFrame (γ = 0.05–0.25), matching your notebook exactly

### Output

| gamma | R0 | peak_infected | peak_day | total_deaths | epidemic_duration |
|------:|---:|--------------:|---------:|-------------:|------------------:|
| 0.05 | 6.00 | 478.63 | 29 | 165.40 | 143 |
| 0.10 | 3.00 | 267.26 | 31 | 83.52 | 106 |
| 0.15 | 2.00 | 134.08 | 35 | 47.58 | 103 |
| 0.20 | 1.50 | 53.82 | 42 | 25.70 | 114 |
| 0.25 | 1.20 | 13.66 | 46 | 10.58 | 136 |

---

## 3. Part 2 — Scenario comparison
- Result tables for Scenario A (High Transmission) and Scenario B (Low Transmission)

### Scenario A — High Transmission

| gamma | R0 | peak_infected | peak_day | total_deaths | epidemic_duration |
|------:|---:|--------------:|---------:|-------------:|------------------:|
| 0.05 | 8.00 | 520.58 | 21 | 284.76 | 118 |
| 0.10 | 4.00 | 340.14 | 22 | 159.89 | 86 |
| 0.15 | 2.67 | 213.47 | 24 | 102.61 | 77 |
| 0.20 | 2.00 | 123.89 | 27 | 67.42 | 78 |
| 0.25 | 1.60 | 63.05 | 30 | 42.69 | 84 |

### Scenario B — Low Transmission

| gamma | R0 | peak_infected | peak_day | total_deaths | epidemic_duration |
|------:|---:|--------------:|---------:|-------------:|------------------:|
| 0.05 | 4.00 | 371.36 | 44 | 88.23 | 178 |
| 0.10 | 2.00 | 139.33 | 52 | 36.70 | 154 |
| 0.15 | 1.33 | 31.34 | 67 | 13.64 | 185 |
| 0.20 | 1.00 | 5.00 | 0 | 1.83 | 116 |
| 0.25 | 0.80 | 5.00 | 0 | 0.43 | 28 |

- Which scenario is worse for public health, and why 


Scenario A is significantly worse in all metrics due to its higher transmission (beta=0.4) and mortality (mu=0.02) rates. Scenario A reaches a peak of 521 infections, which creates a much higher burden on healthcare, compared to only 371 in Scenario B. Also, Scenario A results in 285 total deaths, compared to only 88 in B.
Moreover, at the highest tested recovery rate (gamma=0.25), Scenario A's R0 is 1.6, meaning the epidemic can still grow, while Scenario B's R0 goes down to 0.8, meaning infections are expected to decline.

---

## 4. Part 3 — Policy recommendations
- 4.1 Parameter impact analysis

Increasing the recovery rate improves the epidemic outcomes in both scenarios. In Scenario A, when gamma increases from 0.05 to 0.25, the peak number of infected people decreases from about 521 to 63, while total deaths decrease from about 285 to 43. The epidemic duration also becomes shorter overall, from 118 days at gamma = 0.05 to around 77–84 days for gamma values between 0.15 and 0.25. The same pattern can also be seen in Scenario B. The peak decreases from about 371 infected people at gamma = 0.05 to only 5 at gamma = 0.25, and total deaths decrease from about 88 to less than 1. The epidemic duration changes from 178 days to 28 days. Overall, a higher recovery rate means that infected people leave the infected compartment faster, which results in lower infection peaks and fewer deaths. The epidemic also generally becomes shorter, although the duration does not decrease perfectly with every increase in gamma.

- 4.2 Intervention analysis

Using gamma = 0.10 as the baseline recovery rate for Scenario A, a 50% increase gives a new recovery rate of gamma = 0.15. At gamma = 0.10, the model results in about 160 total deaths, while at gamma = 0.15 this decreases to about 103 deaths. This means that increasing the recovery rate by 50% reduces the total number of deaths by about 57, which is approximately a 35.8% reduction.

- 4.3 Real-world application

One real medical intervention that could increase the recovery rate is antiviral medication. Antiviral drugs can help the body fight a viral infection by reducing how quickly the virus reproduces, which can shorten the time a person stays infected and therefore increase the recovery rate. The actual effectiveness would depend on the disease and the specific treatment, so it is not possible to give one realistic percentage for all cases. In the model, a successful antiviral treatment would be represented by a higher gamma, meaning that infected people move into the recovered group faster. This would be expected to reduce the number of infected people and also lower the number of deaths.

---

## 5. Conclusions
Overall, the results show that increasing the recovery rate makes the epidemic less severe, with lower infection peaks, fewer deaths, and generally a shorter epidemic duration. Scenario A had worse outcomes than Scenario B because of its higher transmission and mortality rates. The intervention analysis also showed that increasing the recovery rate can noticeably reduce the impact of the epidemic. However, this is still a simplified model, so real epidemic outcomes would depend on many other factors as well.