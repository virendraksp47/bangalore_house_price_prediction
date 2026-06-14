# 🏠 Bangalore House Price Prediction

An end-to-end Machine Learning project that predicts house prices in Bangalore based on property features such as location, total square footage, number of bedrooms (BHK), and bathrooms.

This project demonstrates the complete Machine Learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, outlier removal, model selection using Linear Regression, Ridge Regression, and Lasso Regression, Flask web application development, Docker containerization, and deployment on Render.

---

## 🚀 Live Demo

🔗 [https://bangalore-house-price-prediction.com](https://bangalore-house-price-prediction-jwyk.onrender.com/)

---

## 📖 Project Overview

Real estate prices in Bangalore vary significantly depending on location, area, and property characteristics. The objective of this project is to build a machine learning model capable of accurately predicting house prices using historical housing data.

The project follows a complete ML pipeline:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Outlier Detection & Removal
- Model Training & Selection
- Web Application Development using Flask
- Docker Containerization
- Deployment on Render

---

## 🎯 Problem Statement

Predict the price of a house in Bangalore using:

- Location
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-Learn
- Linear Regression
- Ridge Regression
- Lasso Regression

### Web Development
- Flask
- HTML

### Deployment & DevOps
- Docker
- Render
- GitHub

---

## 📊 Dataset

The dataset contains residential property information from various locations in Bangalore.

### Features

| Feature | Description |
|----------|------------|
| location | Property location |
| total_sqft | Total area in square feet |
| bath | Number of bathrooms |
| bhk | Number of bedrooms |
| price | House price in Lakhs |

---

## 🔍 Data Cleaning & Preprocessing

Several preprocessing steps were performed to improve data quality:

- Removed irrelevant columns
- Handled missing values
- Standardized location names
- Converted area values into numeric format
- Reduced location dimensionality
- Created BHK feature
- Encoded categorical variables using One-Hot Encoding

---

## 📈 Exploratory Data Analysis (EDA)

EDA was performed to understand data distribution and identify patterns.

### Analysis Performed

- House price distribution
- Location-wise price trends
- BHK distribution
- Price per square foot analysis
- Correlation analysis
- Scatter plots and histograms
- Outlier visualization

### Key Insights

- Location significantly influences property prices.
- Certain locations contain extreme price outliers.
- Price generally increases with area and BHK count.

---

## 🚨 Outlier Removal

To improve model performance, outliers were identified and removed using:

### Price Per Square Foot Analysis

Removed houses with unrealistic price-per-square-foot values.

### BHK-Based Filtering

Removed properties where larger houses were priced significantly lower than smaller houses in the same locality.

### Statistical Methods

Applied standard deviation-based filtering to eliminate anomalous records.

These techniques helped improve model accuracy and reduce noise in the dataset.

---

## ⚙️ Feature Engineering

Additional features were created to improve predictive performance:

- BHK Feature
- Price Per Square Foot
- Location Encoding using One-Hot Encoding

---

## 🤖 Machine Learning Models

Three regression algorithms were evaluated:

### 1. Linear Regression

A baseline model used to understand the relationship between house features and prices.

### 2. Ridge Regression

Applied L2 regularization to reduce overfitting and improve generalization.

### 3. Lasso Regression

Applied L1 regularization and feature selection by shrinking less important coefficients to zero.

---

## 📊 Model Selection

Multiple models were compared using Cross Validation.

| Model | Purpose |
|---------|----------|
| Linear Regression | Baseline Model |
| Ridge Regression | Regularization |
| Lasso Regression | Feature Selection & Regularization |

After evaluation, the best-performing model Ridge Regression was selected and saved for deployment.

> Replace this section with your actual best model and scores.

---

## 📈 Model Evaluation

### Evaluation Metrics

- R² Score
- Cross Validation Score

Example:

| Model | R² Score |
|---------|---------|
| Linear Regression | 84% |
| Ridge Regression | 86% |
| Lasso Regression | 85% |

> Update with your actual results.


---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Bangalore-House-Price-Prediction.git
cd Bangalore-House-Price-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🐳 Docker Containerization

### Build Docker Image

```bash
docker build -t bangalore-house-price-predictor .
```

### Run Docker Container

```bash
docker run -p 5000:5000 bangalore-house-price-predictor
```

Application URL:

```text
http://localhost:5000
```

---

## ☁️ Deployment on Render

The application is deployed on Render using Docker.

### Deployment Steps

1. Push code to GitHub
2. Create a Web Service on Render
3. Connect GitHub repository
4. Select Docker deployment
5. Deploy application

Render automatically builds and deploys the Docker container.

---

## 🔄 Application Workflow

```text
User Input
     │
     ▼
Flask Application
     │
     ▼
Data Preprocessing
     │
     ▼
Trained Regression Model
     │
     ▼
Price Prediction
     │
     ▼
Display Result
```

---

## 📸 Screenshots

### Home Page

Add screenshot here

### Prediction Result

Add screenshot here

---

## 🎓 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Outlier Detection & Removal
- Machine Learning
- Linear Regression
- Ridge Regression
- Lasso Regression
- Cross Validation
- Model Selection
- Flask Development
- Docker
- Cloud Deployment
- End-to-End ML Pipeline

---

## 🔮 Future Improvements

- Random Forest Regression
- XGBoost Regression
- Hyperparameter Tuning
- CI/CD Pipeline
- Kubernetes Deployment
- Real-Time Data Integration
- Interactive Dashboard

---

## 👨‍💻 Author

**Your Name**

GitHub: [https://github.com/virendraksp47](https://github.com/virendraksp47)

LinkedIn: [https://linkedin.com/in/virendra-kashyap-429b30247](https://www.linkedin.com/in/virendra-kashyap-429b30247/)

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further improvements.

---

### Built with ❤️ using Python, Scikit-Learn, Flask, Docker, and Render.
