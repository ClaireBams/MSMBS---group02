# Network biology

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 02

---

## 1. Repository overview

- `network_biology.ipynb` – analysis of the normal and mutated Boolean networks
- `requirements.txt` – Python dependencies required to run the notebook
- `README.md` – this file

**How to run**: 
--- Install the required dependencies using: `pip install -r requirements.txt`
Then open `network_biology.ipynb` and run the notebook from top to bottom.

## 2. Normal network

The normal network was used as the baseline. The healthy and oncogene-hijacked scenarios resulted in growth, while the stressed scenario activated p53 and cell death. Three attractors were found: healthy growth (128 states), cell death (120 states), and cancer-like growth (8 states). Therefore, 3.1% of the 256 initial states led to cancer-like growth.

## 3. Mutation A – p53 knockout

Briefly describe the mutation.

### Scenario analysis

Results for Healthy, Stressed, and Oncogene Hijacked scenarios.

### Attractor analysis

Number/type of attractors, basin sizes, and percentage of states leading to cancer-like states.

---

## 4. Mutation B – MYC amplification

### Scenario analysis

### Attractor analysis

---

## 5. Mutation C – MDM2 overexpression

### Scenario analysis

### Attractor analysis

---

## 6. Mutation D – [name of your mutation]

Explain why this mutation was chosen.

### Scenario analysis

### Attractor analysis

---

## 7. Comparison

Summary table comparing the normal network and all four mutations.

### Which mutation is most dangerous?

Answer using the percentage of initial states leading to cancer-like attractors.

### Role of feedback loops

Discuss relevant feedback interactions, for example MYC → MDM2 ─| p53.

### Limitations of the Boolean model

1. ...
2. ...
3. ...

---

## 8. Conclusion