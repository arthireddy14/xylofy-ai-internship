# 👨‍💼 Employee Attrition Prediction using Machine Learning

## 📌 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. When experienced employees leave, companies spend significant time and money on hiring, training, and maintaining productivity.

The objective of this project is to build a Machine Learning model that predicts whether an employee is likely to leave the company based on various workplace and employee-related factors. The goal is to help Human Resources (HR) teams identify at-risk employees early so that they can take proactive steps to improve employee retention.

This project was completed as **Week 2** of the **XYlofy AI Internship Program**.

---

# 🎯 Problem Statement

Predict whether an employee will leave the organization based on factors such as:

- Job Role
- Business Travel
- Monthly Income
- Work-Life Balance
- Total Working Years
- Overtime
- Marital Status
- Education
- Job Satisfaction
- and several other employee attributes.

The final solution provides both predictive insights and practical business recommendations for HR teams.

---

# 📂 Dataset

**Dataset:** IBM HR Analytics Employee Attrition Dataset

- Total Records: **1,470 Employees**
- Target Variable: **Attrition (Yes / No)**
- Source: Kaggle

The dataset contains employee demographic information, work-related attributes, compensation details, job satisfaction measures, and performance indicators.

---

# 🛠 Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📋 Project Workflow

The project was completed in multiple stages.

## 1️⃣ Data Loading & Exploration

- Loaded the HR dataset using Pandas.
- Displayed the first few records.
- Checked dataset dimensions.
- Identified numerical and categorical columns.
- Calculated the employee attrition rate.
- Observed that the dataset is imbalanced because significantly fewer employees left compared to those who stayed.

---

## 2️⃣ Data Cleaning & Preprocessing

To prepare the data for Machine Learning:

- Checked for missing values.
- Removed unnecessary columns such as:
  - EmployeeNumber
  - Over18
  - StandardHours
- Converted the target variable:
  - Yes → 1
  - No → 0
- Applied One-Hot Encoding to categorical variables.
- Standardized numerical features using StandardScaler.

Proper preprocessing improves model performance and ensures the data is suitable for machine learning algorithms.

---

## 3️⃣ Exploratory Data Analysis (EDA)

Several visual analyses were performed to understand employee behavior.

The analysis explored:

- Attrition by Department
- Attrition by Job Role
- Monthly Income vs Attrition
- Work-Life Balance vs Attrition
- Years at Company vs Attrition

These analyses helped identify employee groups with higher attrition risk.

---

## 4️⃣ Machine Learning Models

Three classification algorithms were trained and compared.

### Logistic Regression

A simple and interpretable baseline model suitable for HR decision-making.

### Random Forest Classifier

An ensemble learning algorithm capable of identifying complex relationships between employee features.

### Gradient Boosting Classifier

A boosting algorithm designed to improve prediction performance through sequential learning.

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

To address class imbalance, supported models were trained using:

```python
class_weight='balanced'
```

---

## 5️⃣ Model Evaluation

Each model was evaluated using multiple performance metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

The models were compared to determine which one best identified employees likely to leave.

---

## 6️⃣ Feature Importance Analysis

The best-performing model was analyzed to understand which employee characteristics most influenced attrition predictions.

### Top Factors Influencing Employee Attrition

- Overtime
- Frequent Business Travel
- Laboratory Technician Job Role
- Sales Representative Job Role
- Research Director Job Role
- Education Field
- Marital Status
- Total Working Years

Understanding these factors enables HR teams to design targeted retention strategies.

---

## 📊 Visualizations

The project includes several visualizations to better understand employee attrition.

Generated charts include:

- Attrition Rate by Department
- Attrition Rate by Job Role
- Monthly Income Distribution
- Confusion Matrix
- Top 10 Feature Importance
- ROC Curve Comparison

These visualizations provide both technical insights and business understanding.

---

# 💡 Key Business Insights

From the analysis, several important findings emerged:

- Employees working overtime were significantly more likely to leave.
- Frequent business travel increased attrition risk.
- Laboratory Technicians and Sales Representatives showed comparatively higher attrition.
- Salary influenced employee turnover, but workplace conditions and job responsibilities had a stronger impact.
- Employee retention depends on multiple workplace factors rather than compensation alone.

---

# 📈 Business Recommendations

Based on the findings, the following recommendations are suggested:

- Monitor employees with excessive overtime and improve workload distribution.
- Provide better work-life balance initiatives.
- Conduct regular retention discussions with employees in high-risk roles.
- Improve career development opportunities and mentoring programs.
- Offer targeted support for employees who frequently travel for work.

Implementing these recommendations can improve employee satisfaction and reduce turnover.

---

# 📁 Project Structure

```
Week-2-Employee_Attrition_Prediction/
│
├── employee_attrition_prediction.ipynb
├── HR_Attrition.csv
├── summary_employee_attrition_analysis.pdf
├── summary_employee_attrition_analysis.docx
├── charts/
│   ├── attrition_department.png
│   ├── attrition_jobrole.png
│   ├── confusion_matrix.png
│   ├── monthly_income_boxplot.png
│   ├── roc_curve.png
│   └── top10_features.png
└── README.md
```

---

# 🚀 How to Run the Project

1. Clone the repository.

```
git clone https://github.com/arthireddy14/xylofy-ai-internship.git
```

2. Navigate to the Week 2 project folder.

3. Install the required libraries.

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

4. Open the notebook.

```
jupyter notebook
```

5. Run all notebook cells sequentially.

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Classification algorithms
- Model comparison
- Feature importance analysis
- Data visualization
- Translating technical findings into business recommendations

This project strengthened my understanding of applying Machine Learning to solve real-world HR analytics problems.

---

# 👩‍💻 Author

**Arthi Reddy**

AI & Data Science Intern

**Internship:** XYlofy AI Internship Program

GitHub: https://github.com/arthireddy14

---

## ⭐ If you found this project useful, consider giving the repository a Star!
