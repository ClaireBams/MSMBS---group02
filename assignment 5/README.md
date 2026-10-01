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

[Explain in your own words how wall stiffness changes as a function of
chemical level.]

### Pathogen Cells

[Explain what the pathogen does differently.]

---

## 3. Cell-to-Cell Transport and Feedback

### Diffusion Coefficient

[Explain how the diffusion coefficient is defined in the model.]

### Feedback Loop

[Explain the sequence:

chemical → wall stiffness → diffusion → chemical spreading
]

### Feedback Diagram

[Insert sketch/diagram here.]

### Type of Feedback

[State whether this is positive or negative feedback and explain why.]

---

## 4. Effect of `rel_cell_div_threshold`

Two simulations were performed using different values of
`rel_cell_div_threshold`.

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

[Explain how changing the threshold affected the speed of pathogen
population growth.]

---

## 5. Cell Neighbours

[Explain the fundamental difference between cell neighbours in this
model and the models used previously in the course.]

---

## 6. Proposed Plant Defense Mechanism

The proposed defense causes cells with a chemical level above a certain
threshold to stiffen their walls.

### Pseudocode

```text
CellHouseKeeping:

    [existing section ...]

    if [chemical condition]:
        [change wall stiffness]

    [remaining section ...]