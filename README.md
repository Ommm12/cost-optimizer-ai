# 🚀 AI-Powered AWS Cost Optimization System


![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![DevOps](https://img.shields.io/badge/DevOps-CI/CD-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 📌 Overview

This project is a **production-level DevOps + AI system** that monitors AWS costs, detects anomalies, and provides real-time insights through a live dashboard.

It automates cost tracking using AWS services and visualizes data using a Streamlit dashboard deployed on EC2 with a full CI/CD pipeline.

---

## 🎯 Problem Statement

Managing AWS costs manually is inefficient and error-prone.

👉 This system solves that by:
- Automating cost monitoring  
- Detecting unusual spending  
- Providing real-time visibility  
- Reducing manual effort  

---

## 🏗️ Architecture


GitHub → CI/CD → EC2 (Streamlit Dashboard)
↓
AWS Lambda
↓
AWS Cost Explorer API
↓
S3 (store reports)
↓
SNS (Email Alerts)


---

## ⚙️ Tech Stack

### ☁️ Cloud
- AWS EC2 (Hosting Dashboard)
- AWS Lambda (Automation)
- AWS S3 (Storage)
- AWS SNS (Notifications)
- AWS IAM (Security)

### 🧠 Backend
- Python
- Boto3

### 📊 Frontend
- Streamlit
- Plotly

### 🔁 DevOps
- Git & GitHub
- GitHub Actions (CI/CD)
- PM2 (Process Manager)

---

## 🚀 Features

### 🔹 Automation
- Fetch AWS cost data using Lambda  
- Scheduled execution using EventBridge  

### 🔹 Alerts
- Email alerts via SNS  
- Detect high-cost usage  

### 🔹 Storage
- Reports stored in S3  
- Historical cost tracking  

### 🔹 Dashboard
- Live AWS cost dashboard  
- KPI metrics (latest, avg, max cost)  
- Cost trend visualization  
- Interactive charts  

### 🔹 AI Logic
- Cost anomaly detection  
- Trend-based analysis  
- Smart insights (increasing / stable cost)

### 🔹 DevOps
- CI/CD pipeline using GitHub Actions  
- Auto deployment to EC2  
- PM2 for continuous app running  

---

## 📊 Dashboard Preview

> Add screenshots here (important)

---

## 🌐 Live Demo

👉 http://54.224.187.94:8501

---

## 🔁 CI/CD Workflow


Code Push → GitHub → GitHub Actions → EC2 → Deploy → Restart App


---

## 🔐 Security

- Used IAM roles instead of access keys  
- No credentials stored in code  
- GitHub Secrets used for SSH access  

---

## 📂 Project Structure


cost-optimizer-ai/
│
├── dashboard.py
├── lambda_function.py
├── cost_analyzer.py
├── test.py
├── requirements.txt
│
├── .github/workflows/
│ └── deploy.yml
│
└── README.md


---

## 🧪 How to Run Locally

```bash
git clone https://github.com/your-username/cost-optimizer-ai.git
cd cost-optimizer-ai

python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python -m streamlit run dashboard.py

**☁️ Deployment (AWS)**
Launch EC2 instance
Install dependencies
Clone repository
Run Streamlit app
Use PM2 for background execution
Setup GitHub Actions for CI/CD

**📈 Future Improvements**
Machine Learning-based cost prediction
Multi-account AWS monitoring
Slack / Teams integration
Kubernetes deployment
Role-based dashboard access

**💡 Key Learnings**
End-to-end DevOps pipeline
AWS service integration
CI/CD automation
Cloud security best practices
Real-world debugging and deployment

**🎯 Impact**
Reduced manual cost monitoring
Enabled real-time cost visibility
Improved cloud cost efficiency
Built production-ready DevOps system

👨‍💻** Author**: Om Doifode:
GitHub: https://github.com/Ommm12
LinkedIn: (https://www.linkedin.com/in/omdoifode/)
