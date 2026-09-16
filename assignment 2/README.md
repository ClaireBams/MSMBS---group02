# Metabolic modeling

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 02

---

## 1. Repository overview

- `metabolic_modelling.ipynb` – main notebook containing the implementation and answers for Tasks 1–4
- `KEN3170_Assignment_2026_e_coli_core_expression.csv` – maximal reaction activity data used in the assignment
- `e_coli_core.json` – E. coli core metabolic model used in COBRApy
- `requirements.txt` – Python dependencies required to run the notebook
- `README.md` – this file

**How to run**: 
--- Install the required dependencies using: `pip install -r requirements.txt`
Then open `metabolic_modelling.ipynb` and run the notebook from top to bottom.

## 2. Task 1

The maximal reaction activities were visualized on the E. coli core ESCHER map. The values represent max reaction capacities rather than actual FBA fluxes, so they do not have to be equal along a pathway. Grey reactions indicate either zero estimated activity (0.00) or missing activity data (nd).

---

## 3. Task 2 – Enzyme activity-constrained model

The maximal reaction activity data from the CSV file was integrated into the E. coli core model by modifying the reaction flux bounds.

- Reversible reactions were assigned bounds from `-activity` to `+activity`.
- Irreversible reactions kept a lower bound of `0`, while their upper bound was set to the maximal reaction activity.
- Reactions without activity data kept their original model constraints.
- The glucose exchange reaction `EX_glc__D_e` was reset to the high default absolute bounds.
- The lower bound of the ATP maintenance reaction `ATPM` was left unchanged.

The activity dataset contains values for 65 reactions, while the complete E. coli core model contains 95 reactions. Therefore, the final bounds table includes all 95 reactions, with the original constraints retained for reactions without activity data.

---

## 4. Task 3 

---

## 5. Task 4

---

## 6. Conclusions