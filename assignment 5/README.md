# Plant Tissue Simulations

**Course:** KEN3170 – Multi-scale Modeling of Biological Systems  
**Group:** 02

---

## 1. Pathogen Infection Simulation

The `pathogen_infection` model was simulated for a total duration of 2 hours.
Screenshots were taken at the initial state and every 30 minutes.

### 1.1 Simulation Progression

#### 0 minutes
![Initial state](images/infection_0min.png)

**Observation:**  
[Describe the initial tissue and infected region.]

#### 30 minutes
![30 minutes](images/infection_30min.png)

**Observation:**  
[Describe what changed.]

#### 60 minutes
![60 minutes](images/infection_60min.png)

**Observation:**  
[Describe what changed.]

#### 90 minutes
![90 minutes](images/infection_90min.png)

**Observation:**  
[Describe what changed.]

#### 120 minutes
![120 minutes](images/infection_120min.png)

**Observation:**  
[Describe what changed.]

### 1.2 Overall Observations

**Spread of the infected region:**  
[Describe how the infection spreads over the two hours.]

**Tissue deformation:**  
[Describe how the shape/structure of the tissue changes.]

---

## 2. Cell Wall Stiffness

### Normal Cells

For normal cells, the wall stiffness decreases as the chemical level increases. The code first takes the chemical level and scales it by dividing it by 0.5. If this scaled value is above 0.1, the cell wall starts to weaken. The normal stiffness value is 3, and the scaled chemical level is subtracted from this value, so a higher chemical level means a lower wall stiffness. The chemical effect is limited to a maximum value of 1.2, which means the stiffness cannot decrease below 1.8. So overall, the more chemical reaches a normal cell, the softer its wall becomes.

### Pathogen Cells

Pathogen cells are treated differently because the wall weakening rule does not apply to them. The code only reduces stiffness when the cell is not a pathogen (CellType != 2). Because of this, pathogen cells keep the default stiffness value of 3 even when the chemical level is high. So the chemical mainly weakens the surrounding plant cells, while the pathogen itself keeps its wall stiffness unchanged.   Infection

---

## 3. Cell-to-Cell Transport and Feedback

### Diffusion Coefficient

[Explain how the diffusion coefficient is defined in the model.]

### Feedback Loop

[Explain the sequence: chemical → wall stiffness → diffusion → chemical spreading]

### Feedback Diagram

[Insert sketch/diagram here.]

### Type of Feedback

[State whether this is positive or negative feedback and explain why.]

---

## 4. Effect of `rel_cell_div_threshold`

Two simulations were performed using different values of `rel_cell_div_threshold`.

### Run 1 – Lower Threshold

**Value:** `[value]`

![Lower threshold](images/lower_threshold.png)

**Observation:**  
[Describe pathogen population expansion.]

### Run 2 – Higher Threshold

**Value:** `[value]`

![Higher threshold](images/higher_threshold.png)

**Observation:**  
[Describe pathogen population expansion.]

### Comparison

[Explain how changing the threshold affected the speed of pathogen population growth.]

---

## 5. Cell Neighbours

[Explain the fundamental difference between cell neighbours in this model and the models used previously in the course.]

---

## 6. Proposed Plant Defense Mechanism

### Pseudocode

The defense would be added in the same part of `CellHouseKeeping` where the chemical level is checked and the wall stiffness is changed. 


```
calculate chemical level
set normal wall stiffness

if cell is not a pathogen:
    if chemical > defense threshold:
        increase wall stiffness
    else if chemical > weakening threshold:
        decrease wall stiffness
    else:
        keep normal wall stiffness

apply stiffness to the wall
```

So basically, the new condition would be added before the original weakening rule. If the chemical level becomes high enough to activate the defense, the cell would stiffen its wall. If the defense threshold is not reached, the cell would continue following the original rule, where increasing chemical makes the wall weaker.

### Feedback
This defense would add negative feedback. In the original model, more chemical makes the wall less stiff, and a lower stiffness increases the diffusion coefficient, which helps the chemical spread further. With the defense, once the chemical level becomes high enough, the cell reacts in the opposite way and makes its wall stiffer. Since the diffusion coefficient decreases when stiffness increases, this would slow down the spread of the chemical to neighbouring cells. 

more chemical
→ defense is activated
→ wall becomes stiffer
→ diffusion decreases
→ chemical spreads more slowly