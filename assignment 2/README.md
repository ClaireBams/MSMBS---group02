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
- Prepared a plot showing the maximal biomass production rate as a function of the glucose exchange reaction flux bound in the interval [1, 15] mmol/gDW/h with increments of 0.1.
- Observed that the growth rate does not increase indefinitely. The curve eventually plateaus because the internal enzymes reach their maximum capacity limits, preventing the cell from processing additional glucose any faster.
- Inspected the exchange reaction fluxes and identified that in the second segment, the cell shifts to overflow metabolism, activating the acetate exchange reaction (`EX_ac_e`) to secrete excess carbon.

## 6. Conclusions
Adding enzyme activity limits to the model shows a much more realistic behavior of the cell. Cell growth depends mainly on two factors: the amount of glucose available outside and the capacity of the enzymes inside. 
As we increased the glucose supply, the main respiratory pathways of the cell reached their limit. To process the excess carbon, the cell switched to a fermentation metabolism and started secreting acetate (`EX_ac_e`). 
Finally, the system reached a maximum point where more glucose no longer increases the growth rate. This shows that the internal enzymes are working at their maximum capacity.