# Veekstar Retail Intelligence

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)
A modern retail analytics platform that transforms raw business data into actionable insights through interactive dashboards, forecasting models, and secure access control.

---

##  Live Application

[Launch Dashboard](https://veekstar-retail-insights.streamlit.app)

No installation required — access the full system directly in your browser.

---

##  Core Capabilities

This system provides end-to-end retail intelligence for decision-making:

* Sales performance tracking
* Customer segmentation analysis
* Inventory monitoring and stock insights
* Predictive sales forecasting
* KPI visualization for executives
* Secure authentication system with role-based access control

---

##  Authentication & Access Control

This system includes a secure login layer to ensure controlled access:

* User authentication via Streamlit Authenticator
* Session-based login management
* Protected dashboard routes
* Logout control (desktop + mobile optimized)
* Prevents unauthorized access to business data

---

##  Dashboard Preview

### Overview Dashboard

![Overview](assets/screenshots/overview.jpg)

---

### Sales Intelligence

![Sales](assets/screenshots/sales.jpg)

---

### Forecasting Engine

![Forecast 1](assets/screenshots/forecast1.jpg)

![Forecast 2](assets/screenshots/forecast2.jpg)

---

### Performance Analytics

![Performance](assets/screenshots/performance.jpg)

---
## 📖 Project Story

Retail businesses often struggle with understanding their data in a meaningful way. Most of the time, information is scattered across spreadsheets, making it difficult to track performance, identify trends, or make fast decisions.

This project was built to solve that problem.

Instead of relying on static reports, Veekstar Retail Intelligence brings everything into one interactive system where business owners can:

* See what is happening in real time
* Understand why it is happening
* And predict what will happen next

The goal was not just to build a dashboard, but to design a **decision-making tool** that feels simple enough for non-technical users, yet powerful enough for analytical work.

Every feature was intentionally designed around clarity, speed, and business usefulness — not just visualization.



This project demonstrates how data can be transformed into real business intelligence when structured properly.

## 🛠 Tech Stack

**Core:**

* Python
* Streamlit
* Pandas
* Plotly

**Machine Learning & Forecasting:**

* Scikit-learn
* Joblib
* Statsmodels *(if used in forecasting models)*

**Security:**

* Streamlit Authenticator
* YAML-based credential management

---

##  Business Value

This platform helps business owners and analysts answer critical questions:

* What products are driving revenue?
* How are customers behaving over time?
* What inventory risks exist?
* What will future sales look like?

It replaces manual spreadsheet analysis with a real-time decision system.

---

##  Case Study (How This System Was Built)

This project was designed as a full retail intelligence system with the following architecture:

1. **Data Layer**

   * Cleaned and structured retail transaction data

2. **Analytics Layer**

   * Aggregations using Pandas
   * KPI computations (sales, customers, inventory trends)

3. **Visualization Layer**

   * Interactive charts built with Plotly

4. **Machine Learning Layer**

   * Forecasting models for future sales trends

5. **Application Layer**

   * Streamlit dashboard for real-time interaction
   * Authentication system for secure access

This makes it a complete end-to-end business intelligence solution, not just a visualization tool.

---

##  Run Locally

```bash id="runfinal01"
git clone https://github.com/veekstar-tech/veekstar_retail_insights.git
cd veekstar_retail_insights
pip install -r requirements.txt
streamlit run app.py
```

---

##  Demo Login

Username: guest
Password: veekstar2025

---

## 👤 Author

Veekstar Tech — Data Science & Retail Intelligence Systems
