# 📈 End-to-End Sales Forecasting & Demand Intelligence System

## 📌 Project Overview

This project was completed as part of my **Week 3 & Week 4 AI & Data Science Internship at XYlofy AI**.

The objective was to build a complete demand intelligence system capable of forecasting future sales, detecting unusual sales behavior, segmenting products based on demand, and providing an interactive business dashboard.

The project simulates a real-world retail demand forecasting system similar to those used by companies like Amazon, Walmart, and Flipkart.

---

# 🚀 Features

- Sales Data Cleaning & Exploration
- Time Series Analysis
- Seasonal Decomposition
- Stationarity Testing (ADF)
- Sales Forecasting using:
  - SARIMA
  - Facebook Prophet
  - XGBoost
- Model Performance Comparison
- Product Category & Region Forecasting
- Weekly Sales Anomaly Detection
- Product Demand Segmentation using K-Means
- Interactive Streamlit Dashboard
- Executive Business Report

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Prophet
- XGBoost
- Scikit-learn
- Streamlit
- Git & GitHub

---

# 📊 Best Forecasting Model

Three forecasting models were evaluated.

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| SARIMA | 18031.40 | 19009.18 | 0.1897 |
| Prophet | 20250.79 | 22318.41 | 0.2186 |
| **XGBoost** | **14537.39** | **17093.03** | **0.1459** |

**Selected Model:** XGBoost

It achieved the lowest forecasting error and produced the most accurate predictions.

---

# 📂 Project Structure

```
Week-3-4-Sales-Forecasting-Demand-Intelligence-System/

│
├── analysis.ipynb
├── app.py
├── requirements.txt
├── summary.pdf
├── train.csv
├── forecast_results.csv
├── anomaly_results.csv
├── cluster_results.csv
│
└── charts/
```


---


# 📈 Business Insights

- Technology generated the highest historical revenue.
- Furniture is expected to experience the strongest future growth.
- West region shows higher projected demand.
- XGBoost outperformed SARIMA and Prophet.
- Product demand was successfully segmented into multiple business groups to support inventory planning.

---

# 🔮 Future Improvements

- Real-time forecasting
- Hyperparameter tuning
- Cloud deployment
- Automated model retraining
- Power BI integration

---

# 👨‍💻 Author

**Arthi Reddy**

AI & Data Science Intern — XYlofy AI

GitHub: https://github.com/arthireddy14
