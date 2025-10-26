# Employee Attrition Prediction for Aventra Auto

## 1. Business Problem
Aventra Auto is an industry leader with a recognized high-performance culture. While this culture drives innovation, it has also led to a significant business challenge: **a voluntary turnover rate** that exceeds industry benchmarks.

High attrition introduces significant costs, both direct and indirect, including talent acquisition expenses, onboarding, and the time required for new hires to ramp up. Furthermore, the loss of institutional knowledge and decreased team productivity during transitions represents a cost to the company in millions. The HR team has a clear mandate: reduce voluntary attrition and enhance employee retention.

Currently, the company's retention efforts are reactive, typically initiated during exit interviews. To mitigate this, HR must pivot from a reactive posture to a proactive, data-informed talent management strategy. They require a system to identify flight risks, enabling managers and HRBPs to conduct targeted interventions before an employee resigns.

## 2. Solution Overview
This project addresses Aventra Auto's challenge by building a predictive model as an early warning system for identifying flight risks.

Using historical employee data—including performance metrics, project workload, and employee tenure—I developed a model that quantifies an employee's risk of voluntary turnover. This model provides the HR team with a powerful tool to identify employees with a high propensity for attrition and take action to keep them.

The model's feature importance analysis provides clear, actionable insights into the key drivers of attrition at the company.

## 3. Key Findings
The analysis reveals that voluntary turnover at Aventra Auto is not a single, uniform problem; it is two main types of employees leaving:

1. A significant cohort of departing employees consists of individuals with the highest performance ratings and the heaviest project workloads. These are the company's high-potential employees (HiPo, i.e., top performers). They are not leaving due to poor performance; they are exiting due to burnout. The loss of this group represents a critical erosion of the company's talent pipeline.

2. The second cohort consists of employees with lower performance ratings and significantly lighter workloads. Their departure is symptomatic of disengagement, not enough work, or a mismatch with their role. This trend highlights potential gaps in the company's performance management and career pathing frameworks.

Understanding these two different attrition drivers is the most critical insight from this project. A one-size-fits-all retention strategy will be ineffective. Retaining a high-performer requires interventions focused on workload management and career advancement, while addressing a disengaged employee requires performance coaching and a potential reassessment of role alignment.

## 4. Recommendations
Based on the model's findings, I propose a three-part action plan for the HR team:

| **Recommendation** | **Business impact & HR intervention** |
|---|---|
| Use a dashboard to predict which employees might leave | Enables proactive, targeted interventions. By allowing managers and HRBPs to focus on the 10-15% most likely to leave, this tool could drive a 20-25% reduction in voluntary turnover within the first year. |
| Implement workload planning for high-performers | Directly addresses the high-performer burnout persona. Implementing limit workload and regularly check projects will protect the company's most valuable talent assets, improving long-term innovation and productivity. |
| Launch a mid-tenure career program | Mitigates the predictable spike in attrition among mid-tenure employees. This program will increase employee engagement and organizational commitment, strengthening the internal leadership pipeline and reducing reliance on costly external hiring. |

## 5. Model Performance
The final model is highly effective for its strategic objective. Its KPIs are:

- Overall Accuracy: 96%

- Recall (for Attrition Class): 90%

The high recall score is the most important KPI for this business problem. It confirms the model successfully identifies 9 out of every 10 employees who are genuine flight risks, allowing for effective and timely intervention.

## 6. Source Acknowledgment

This repository originates from the [Google Advanced Data Analytics Capstone (Coursera)](https://www.coursera.org/professional-certificates/google-advanced-data-analytics), with datasets and base structure used under Coursera’s Educational Use Policy.

I assumed full responsibility for **redefining the analytical framework**, ensuring the project meets professional data science standards rather than academic prototypes.  Major contributions include:
- Architecting a refined feature engineering pipeline to eliminate data leakage and improve model interpretability.  
- Designing and validating a new binary feature, `Overworked`, as a proxy for labor intensity and burnout risk.  
- Developing, tuning, and evaluating a high-performing Random Forest Classifier (96.2% accuracy, 96.5% AUC).  
- Translating model insights into strategic workforce recommendations on workload management and tenure-based retention.

> *This repository represents an independently executed and technically upgraded version of the original Coursera project, maintained solely for educational and portfolio demonstration purposes.*



