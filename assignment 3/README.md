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

p53 is off in the case of this mutation.

### Scenario analysis
For the Healthy Cell, Stressed Cell, and Oncogene Hijacked Cell scenarios, the final state is always Growth = 1, Death = 0, and p53 = 0. All three cells grow. The Stressed Cell does not die anymore because p53 is permanently disabled and cannot trigger cell death.

### Attractor analysis
There are 2 attractors in total. Healthy growth accounts for 128 states (50.0%), and cancer-like growth accounts for 50% as well. The Cell death attractor is not included. 50.0% of the initial states end in cancer-like growth, compared with 3.1% in the normal network.


## 4. Mutation B – MYC amplification

MYC is on in mutation B.

### Scenario analysis
For the Healthy Cell, Stressed Cell, and Oncogene Hijacked Cell scenarios, the final state is always Growth = 1, Death = 0, and p53 = 0. All three cells grow. The Stressed Cell does not die anymore because constant MYC activity activates MDM2, which in turn keeps p53 OFF.

### Attractor analysis
There are 2 attractors in total. Healthy growth accounts for 128 states (50.0%), and Cancer-like growth accounts for the other half. 50.0% of the initial states end in cancer-like growth, in contrast with 3.1% in the normal network.

## 5. Mutation C – MDM2 overexpression

MDM2 is always ON in this mutation.

### Scenario analysis

| Scenario | Growth | Death | p53 |
|---|---|---|---|
| Healthy Cell | 1 | 0 | 0 |
| Stressed Cell | 1 | 0 | 0 |
| Oncogene Hijacked Cell | 1 | 0 | 0 |

All three cells grow. The Stressed Cell does not die anymore, because MDM2 keeps p53 OFF.

### Attractor analysis

| Attractor | Classification | Basin size | Basin percentage |
|---|---|---|---|
| 1 | Healthy growth | 128 | 50.0% |
| 2 | Cancer-like growth | 128 | 50.0% |

The Cell death attractor is gone. 50.0% of the states (128 out of 256) end in cancer-like growth, compared with 3.1% in the normal network.

---

## 6. Mutation D – p21 (CDKN1A) knockout

We picked p21 because it is the cell's normal "brake". In real cancer cells, losing p21 is known to remove this brake.(https://pmc.ncbi.nlm.nih.gov/articles/PMC2722839/)
### Scenario analysis

| Scenario | Growth | Death | p53 |
|---|---|---|---|
| Healthy Cell | 1 | 0 | 0 |
| Stressed Cell | 0 | 1 | 0 |
| Oncogene Hijacked Cell | 1 | 0 | 0 |

The Stressed Cell still dies here, but it never fully settles, it keeps oscillating, so this row only shows its state after 15 steps.

### Attractor analysis

| Attractor | Classification | Basin size | Basin percentage |
|---|---|---|---|
| 1 | Healthy growth | 128 | 50.0% |
| 2 | Cell death | 24 | 9.4% |
| 3 | Cancer-like growth | 8 | 3.1% |

Cell death drops a lot compared to the normal network (46.9% -> 9.4%). This drop (120 to 24 states, a difference of 96) matches almost exactly the 96 states (37.5%) that no longer reach a steady state, which suggests these are largely the same states: cells that used to die now get stuck oscillating instead. Cancer-like growth stays the same, at 3.1%.


---

## 7. Comparison of all networks

| Network | Cancer-like basin size | Cancer-like percentage |
|---|---:|---:|
| Normal network | 8 | 3.1% |
| p53 knockout | 128 | 50.0% |
| MYC amplification | 128 | 50.0% |
| MDM2 overexpression | 128 | 50.0% |
| p21 knockout | 8 | 3.1% |

The p21 knockout does not increase the cancer-like fixed-point basin, which remains at 3.1%. However, 37.5% of the initial states no longer reach a fixed point and instead show oscillatory behaviour.


### Comparison of cancer-like basin percentages

- The normal network has a cancer-like basin of **3.1%**.
- p53 knockout, MYC amplification, and MDM2 overexpression increase this to **50.0%**, an increase of **46.9 percentage points**.
- The p21 knockout keeps the cancer-like fixed-point basin at **3.1%**, but many states become oscillatory instead of reaching a fixed point.

### Which mutation is the most dangerous?

- The p53 knockout, MYC amplification, and MDM2 overexpression show the strongest effect in this model. For all three mutations, 50.0% of the initial states lead to cancer-like growth, compared with only 3.1% in the normal network.

### What is the role of feedback loops?

- The MYC → MDM2 ─| p53 interaction is important because MYC activates MDM2, while MDM2 inhibits p53. Since p53 normally suppresses growth and promotes cell death, increased MYC or MDM2 activity can keep p53 inactive and favour continued growth.

### What are the limitations of this Boolean model?

- Each node can only be **ON or OFF**, so intermediate levels of gene or protein activity are not represented.
- All nodes are updated at the **same time**, while biological processes can happen at different speeds.
- The network contains only a small number of genes and interactions, so many biological mechanisms and external factors are not included.


---

## 8. Conclusion

Overall, the mutations had a clear effect on the behaviour of the Boolean network. p53 knockout, MYC amplification, and MDM2 overexpression produced the largest increase in cancer-like states, while p21 knockout mainly introduced more oscillatory behaviour. The analysis also shows how feedback interactions can strongly influence cell fate in a simplified regulatory model.