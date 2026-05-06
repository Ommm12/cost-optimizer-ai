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

> <img width="1920" height="1020" alt="Screenshot 2026-05-05 180117" src="https://github.com/user-attachments/assets/bbc1f69e-0acf-40eb-ba75-c4a17c2b2a43" />


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


1. git clone https://github.com/your-username/cost-optimizer-ai.git

2. cd cost-optimizer-ai

3. python -m venv venv

4. source venv/bin/activate   # Linux

5. venv\Scripts\activate      # Windows

6. pip install -r requirements.txt

7. python -m streamlit run dashboard.py

   



**☁️ Deployment (AWS)**

1. Launch EC2 instance

2. Install dependencies

3. Clone repository

4. Run Streamlit app

5. Use PM2 for background execution

6. Setup GitHub Actions for CI/CD

   




**📈 Future Improvements**

1. Machine Learning-based cost prediction

2. Multi-account AWS monitoring

3. Slack / Teams integration

4. Kubernetes deployment

5. Role-based dashboard access






**💡 Key Learnings**

1. End-to-end DevOps pipeline

2. AWS service integration

3. CI/CD automation

4. Cloud security best practices

5. Real-world debugging and deployment

   

   



**🎯 Impact**

1. Reduced manual cost monitoring

2. Enabled real-time cost visibility

3. Improved cloud cost efficiency

4. Built production-ready DevOps system
   
 


👨‍💻** Author**:

Om Doifode:

GitHub: https://github.com/Ommm12

LinkedIn: (https://www.linkedin.com/in/omdoifode/)
