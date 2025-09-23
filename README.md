---

# 🚀 Cloud-Native MLOps Pipeline for Vehicle Insurance Prediction

An **end-to-end Machine Learning Operations (MLOps) pipeline** that automates the **lifecycle of a vehicle insurance prediction model**.
This project demonstrates how to take a raw dataset → preprocess → train → validate → deploy → monitor, all within a **cloud-native CI/CD ecosystem** using **MongoDB, AWS, Docker, and GitHub Actions**.

---

## 📌 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup Guide](#setup-guide)
5. [Pipeline Workflow](#pipeline-workflow)
6. [CI/CD & Deployment](#cicd--deployment)
7. [Results & Future Enhancements](#results--future-enhancements)

---

## 📝 Overview

This project focuses on building a **scalable, production-ready MLOps pipeline** for **vehicle insurance risk prediction**. It goes beyond simple model training by integrating:

* **Data ingestion from MongoDB Atlas**
* **Data validation & transformation pipelines**
* **Model training, evaluation, and versioning**
* **Cloud storage (AWS S3) for model artifacts**
* **Continuous Integration & Continuous Deployment (CI/CD) with GitHub Actions**
* **Containerization with Docker & deployment on AWS EC2**

---

## ✨ Features

✅ Modular project structure with `template.py` scaffolding
✅ Custom **logging & exception handling**
✅ MongoDB Atlas integration for data storage
✅ Automated **Data Ingestion → Validation → Transformation**
✅ Configurable **training pipelines** with reusable entities
✅ **AWS S3 model registry** for version control
✅ End-to-end CI/CD pipeline with **GitHub Actions + Self-Hosted Runner**
✅ Containerized with **Docker** and deployed on **AWS EC2**
✅ Web app for predictions + on-demand training endpoint

---

## 🛠️ Tech Stack

* **Programming Language**: Python 3.10
* **Data Storage**: MongoDB Atlas
* **Cloud Services**: AWS S3, EC2, IAM, ECR
* **Containerization**: Docker
* **CI/CD**: GitHub Actions (self-hosted runner)
* **Environment Management**: Conda
* **Orchestration**: Custom training & prediction pipelines
* **Visualization & EDA**: Jupyter Notebooks
* **Logging & Exception Handling**: Custom modules

---

## ⚙️ Setup Guide

### 1. Project Setup

```bash
# Create virtual environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# Install requirements
pip install -r requirements.txt
pip list
```

Run project scaffolding:

```bash
python template.py
```

---

### 2. MongoDB Atlas Setup

* Create a **MongoDB Atlas Cluster** (M0 free tier).
* Whitelist `0.0.0.0/0` for global access.
* Create DB user & get the **connection string**.
* Push dataset into MongoDB using `mongoDB_demo.ipynb`.
* Verify data inside **MongoDB Collections**.

---

### 3. Logging & Exception Handling

* Test via:

```bash
python demo.py
```

---

### 4. Data Pipeline Components

* **Data Ingestion** → Fetch data from MongoDB, convert to DataFrame.
* **Data Validation** → Schema checks via `config.schema.yaml`.
* **Data Transformation** → Feature engineering & preprocessing.
* **Model Training** → Train ML model & save artifacts.

Set MongoDB URL:

```bash
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"
echo $MONGODB_URL

# PowerShell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"
echo $env:MONGODB_URL
```

---

### 5. AWS Setup

* Create **IAM user** with `AdministratorAccess`.
* Setup AWS credentials:

```bash
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="xxx"
```

* Create **S3 bucket**: `my-model-mlopsproj` for model artifacts.
* Store models under `model-registry`.

---

## 🔄 Pipeline Workflow

1. **Data → MongoDB → Data Ingestion**
2. **Validation → Transformation → Training**
3. **Model Registry on AWS S3**
4. **Evaluation & Thresholding (0.02)**
5. **Best Model pushed for Deployment**
6. **Flask Prediction API → Dockerized → AWS EC2**

---

## 🚀 CI/CD & Deployment

* **Dockerfile & .dockerignore** created for image builds.
* **GitHub Actions** workflow (`aws.yaml`) connects with:

  * **ECR** → Push Docker Image
  * **EC2** → Deploy via Self-Hosted Runner
* **Secrets in GitHub**:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION`
  * `ECR_REPO`

Expose app on EC2:

```bash
Custom TCP → Port 5000 → 0.0.0.0/0
```

Access app:

```
http://<ec2-public-ip>:5000
```

Training endpoint:

```
http://<ec2-public-ip>:5000/training
```

---

## 📊 Results & Future Enhancements

* ✅ End-to-end automated ML pipeline in production.
* ✅ CI/CD with cloud-native deployment.
* 🔮 Future work:

  * Add monitoring with **Prometheus + Grafana**.
  * Enable **multi-model registry** & experiment tracking (MLflow).
  * Expand deployment with **Kubernetes/EKS**.

---

🔥 This project demonstrates the **complete lifecycle of ML in production using MLOps best practices** — from **data to deployment**.

---

