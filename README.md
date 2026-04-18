# 🛡️ Smart Expense Optimizer & Fraud Detector

[![Live Demo](https://img.shields.io/badge/Demo-HuggingFace-orange?style=for-the-badge&logo=huggingface)](https://ak1409-fraud-detection-ai.hf.space)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Dashboard-Power_BI-yellow?style=for-the-badge&logo=powerbi)](https://powerbi.microsoft.com/)

## 📌 Project Overview
A sophisticated financial security system that combines **Unsupervised Machine Learning** with **Business Intelligence**. This project identifies fraudulent transaction patterns in real-time and provides an interactive dashboard for financial auditing and expense optimization.

### 🧠 The Problem
Financial fraud is often like a needle in a haystack—rare but extremely costly. This project uses **Isolation Forest** (Anomaly Detection) to flag suspicious transactions without needing prior "labels" of what fraud looks like.

---

## 📊 Business Intelligence Dashboard
> **Interactive Power BI Dashboard**
> *Analyzed 280,000+ transactions to identify peak fraud windows and high-risk categories.*

![Dashboard Preview](https://github.com/Akansha1409/expense-fraud-detector/blob/main/Screenshot%20(8).png)

### **Key Insights Identified:**
* **Fraud Spikes:** Identified specific time windows (3 AM - 5 AM) where anomalous activity peaked.
* **Financial Exposure:** Visualized the total "at-risk" amount vs. verified transactions.
* **Optimization:** Flagged high-amount outliers for manual review to reduce false positives.

---

## 🛠️ Technical Stack
* **Machine Learning:** Isolation Forest (Scikit-Learn)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Power BI Desktop, Seaborn, Matplotlib
* **Deployment:** Streamlit, Hugging Face Spaces
* **Data Source:** Kaggle Credit Card Fraud Detection Dataset

---

## 📁 Project Structure
```text
├── analysis.ipynb        # Data Cleaning, EDA, & Model Training
├── app.py                # Streamlit Web Application (Live Demo)
├── detector.py           # Python script for real-time terminal testing
├── fraud_model.pkl       # Saved ML Model (Joblib)
├── requirements.txt      # List of dependencies
└── cleaned_fraud_data.csv # Processed data for Power BI
