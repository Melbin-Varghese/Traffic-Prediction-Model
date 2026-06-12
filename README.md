
🚦 Traffic Volume Prediction System

📌 Project Overview

This is an end-to-end Machine Learning project designed to predict traffic congestion levels using environmental and temporal features.

The goal was to simulate a real-world predictive analytics system that could support intelligent traffic management and smart city planning.
📊 Problem Statement

Traffic congestion is influenced by weather conditions, time, and seasonal patterns. This project predicts traffic volume using historical traffic and weather data.
🛠 Tech Stack

Python

Pandas & NumPy

Scikit-learn

Streamlit

Matplotlib / Seaborn

Pipeline

🔍 Feature Engineering

Handled missing values

Extracted time-based features:

Hour

Month

Weekend indicator

Applied One-Hot Encoding for categorical features (weather conditions)

Ensured feature consistency using a structured preprocessing pipeline
🤖 Model Development

Trained multiple regression models

Evaluated using:

R² Score

Mean Absolute Error (MAE)

Selected best-performing model based on accuracy and generalization
🚀 Deployment

Integrated model into a Streamlit web application

Enabled real-time user input and traffic prediction

Prevented feature mismatch using a production-ready preprocessing pipeline
💡 Key Learning Outcomes

Managing training–inference consistency

Handling feature mismatch errors

Building ML pipelines to prevent data leakage

Deploying ML models into interactive web applications
📁 Project structure

traffic-prediction/ │ ├── app.py ├── model.pkl ├── requirements.txt ├── notebook.ipynb └── README.md

## 📸 Project Screenshots

### Main Interface

![Main Interface](screenshots/Interface%201.png)

### Dashboard View

![Dashboard](screenshots/Interface%202.png)

### Data Visualization

![Visualization](screenshots/Interface%203.png)

### Code Interface

![Code](screenshots/Code%20Interface.png)

### Prediction Output

![Output 1](screenshots/Output%201.png)

![Output 2](screenshots/Output%202.png)

