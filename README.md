# Employee Attrition Prediction for Aventra Auto  

<p align="left">

  <!-- Last Commit -->
  <img src="https://img.shields.io/github/last-commit/claire-np/employee-attrition-prediction?color=brightgreen&label=last%20commit" />

  <!-- Python version -->
  <img src="https://img.shields.io/badge/Python-3.10-blue" />

  <!-- Jupyter Notebook -->
  <img src="https://img.shields.io/badge/Notebook-Jupyter-orange" />

  <!-- Project Status -->
  <img src="https://img.shields.io/badge/Status-Completed-success" />

</p>


## 1. Business Problem  
Aventra Auto operates in a fast-paced, high-performance environment. While this culture supports innovation, it has also led to a **voluntary attrition rate above industry norms**.

Turnover is costly—recruitment, onboarding, lost productivity, and loss of institutional knowledge collectively represent a multimillion-dollar risk. More importantly, current retention measures are **reactive**, happening after employees decide to leave.

The HR team needs a way to **identify flight risks early**, enabling targeted, proactive retention efforts.

---

## 2. Solution Overview  
This project builds a predictive model that estimates an employee’s likelihood of voluntary attrition.

Using historical HR records (performance, workload, tenure, promotion history), the model provides a **risk score** for each employee. The goal is to support HRBPs and managers by:

- Highlighting employees at high risk of leaving  
- Allowing timely check-ins and workload adjustments  
- Shifting retention strategy from reactive to proactive  

The model is paired with SHAP-based interpretability to show **why** an employee is at risk, ensuring HR actions are targeted and credible.

---

## 3. Key Insights  
Attrition at Aventra Auto is driven by **two distinct segments**, each requiring different retention strategies:

### **1. High performers with heavy workloads**  
These employees deliver strong results and handle disproportionately high project loads.  
Their exits stem from **burnout**, not poor performance.  
Losing this group weakens innovation, delivery capacity, and succession pipelines.

### **2. Under-engaged employees with low workload and low performance**  
This group shows lower evaluations and minimal project involvement.  
Their departures signal **disengagement or poor role fit**.  
It highlights opportunities to improve performance management and career development.

➡️ **Insight:** Attrition is *not uniform*. A single retention strategy will not work across both groups.

Below are selected visualizations that illustrate the two dominant attrition personas identified in the analysis.

### 📊 Key Attrition Patterns

<table>
<tr>

<td align="center" width="50%">

### <sub><b>Burnout Pattern: High Performers Working Extreme Hours</b></sub>

<img width="100%" alt="High Performers Working Extreme Hours" src="https://github.com/user-attachments/assets/7fc0f4aa-6f0d-484c-9e0c-85fef304df57" />

</td>

<td align="center" width="50%">

### <sub><b>Disengagement Pattern: Low Satisfaction & Low Workload</b></sub>

<img width="100%" alt="Low Satisfaction & Low Workload" src="https://github.com/user-attachments/assets/6af0d3fc-5310-481d-9b9b-fb8f156ba03d" />

</td>

</tr>
</table>

Together, these two patterns highlight that attrition at Aventra Auto stems from opposite employee experiences—burnout among high performers carrying excessive workloads, and disengagement among low-satisfaction employees with minimal responsibilities. Addressing both ends of this spectrum is essential for building an effective, targeted retention strategy.

---

## 4. Recommendations  

| Recommendation | Business Impact |
|---|---|
| **Deploy an attrition-risk dashboard** | Allows HR to monitor the top 10–15% highest-risk employees and intervene early. Expected to reduce voluntary turnover by ~20–25% within a year. |
| **Rebalance workload for high performers** | Reduces burnout and protects critical talent. Preserves innovation capacity and prevents costly replacements. |
| **Launch mid-tenure career pathing initiatives** | Addresses the common “mid-tenure dip” in engagement. Strengthens internal mobility and reduces reliance on external hiring. |

---

## 5. Model Performance

The final Random Forest model performs strongly for HR decision support:

- **Accuracy:** 96%  
- **Recall (Attrition class):** 90%  

High recall is critical in this business context because the priority is to avoid missing employees who are true flight risks.  
A 90% recall means the model correctly identifies **9 out of 10 employees likely to leave**, enabling timely and proactive HR intervention.


### **📊 Feature Importance (Random Forest)**

<p align="center">
  <img width="720" alt="Feature Importance" src="https://github.com/user-attachments/assets/176214ad-85bc-4179-a65b-b591541b6b13" />
</p>

This visualization highlights the strongest drivers of voluntary attrition captured by the Random Forest model.

Performance evaluation scores, Project load, and Tenure are the most influential predictors of whether an employee is likely to leave.  
These findings reinforce the two dominant attrition personas observed in the EDA:  
(1) high-performing employees experiencing workload pressure, and  
(2) low-engagement employees with reduced satisfaction and lighter workloads.


---

## 6. Source Acknowledgment  
This repository originates from the [Google Advanced Data Analytics Capstone (Coursera)](https://www.coursera.org/professional-certificates/google-advanced-data-analytics), with datasets and base structure used under Coursera’s Educational Use Policy.

I assumed full responsibility for **redefining the analytical framework**, ensuring the project meets professional data science standards rather than academic prototypes.  Major contributions include:

- A refined feature engineering pipeline with improved interpretability  
- A new engineered feature (`Overworked`) capturing workload stress  
- A validated Random Forest model achieving >96% accuracy  
- Translation of model insights into actionable HR retention strategies  

> *This repository represents an independently executed and technically upgraded version of the original Coursera project, maintained solely for educational and portfolio demonstration purposes.*



