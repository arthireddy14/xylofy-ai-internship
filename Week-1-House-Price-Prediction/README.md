# Week 1 - Project
# House Price Prediction

## Overview

This project predicts house prices using machine learning techniques based on property features such as area, bedrooms, bathrooms, stories, parking, furnishing status, and other amenities.

## Dataset

Housing Prices Dataset from Kaggle.
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Project Workflow

1. Data Loading & Exploration
2. Data Cleaning
3. One-Hot Encoding
4. Model Building
   - Linear Regression
   - Random Forest Regressor
5. Model Evaluation
6. Visualization
7. Insights & Recommendations

## Results

### Linear Regression

- MAE: 970,043
- RMSE: 1,324,507
- R² Score: 0.653

### Random Forest

- MAE: 1,021,546
- RMSE: 1,400,566
- R² Score: 0.612

## Key Insights

- Area is the strongest predictor of house price.
- Bathrooms and air conditioning significantly influence prices.
- Larger houses generally command higher prices.
- Linear Regression outperformed Random Forest on this dataset.

## Visualizations

### House Price Distribution

![Histogram](house_price_distribution.png)

### Correlation Heatmap

![Heatmap](correlation_heatmap.png)

### Actual vs Predicted Prices

![Prediction](actual_vs_predicted.png)
