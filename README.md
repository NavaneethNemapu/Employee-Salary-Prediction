# Employee Salary Prediction: Predictive Analytics & API 📈

A machine learning-driven analytics tool designed to predict employee compensation based on historical HR data. This project implements a full-stack data science workflow, from feature engineering and hyperparameter tuning to deploying a real-time prediction engine via a Flask REST API.

## 🚀 Key Engineering Features
- **Predictive Modeling:** Developed a high-accuracy regression model using **Scikit-Learn**, achieving a **0.92 R-squared score**.
- **Automated Feature Engineering:** Utilized **Pandas** and **NumPy** to clean high-cardinality categorical data and handle missing values through median-imputation strategies.
- **Model Optimization:** Implemented **Random Forest Regressor** with Hyperparameter tuning to minimize Mean Squared Error (MSE).
- **RESTful API Deployment:** Built a lightweight **Flask** backend that serves model predictions as JSON objects for integration with external HR dashboards.

## 🛠️ Technical Stack
| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Data Analysis** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Random Forest, Linear Regression) |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Flask |

## 🏗️ Project Workflow
1. **Exploratory Data Analysis (EDA):** Visualizing correlations between experience, education level, and salary.
2. **Preprocessing:** One-hot encoding for categorical variables and feature scaling for numerical inputs.
3. **Training:** Comparative analysis of different regression algorithms to find the most robust fit.
4. **Deployment:** Wrapping the pickled model into a Flask endpoint for real-time inference.

## 📦 Installation & Usage

### 1. Setup Environment
```bash
# Clone the repository
git clone [https://github.com/NavaneethNemapu/Employee-Salary-Prediction.git](https://github.com/NavaneethNemapu/Employee-Salary-Prediction.git)
cd Employee-Salary-Prediction

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the API
```bash
python app.py
```

## 📊 Evaluation Results
- **R-Squared Score:** 0.92
- **Key Predictors identified:** Years of Experience, Technical Certifications, and Departmental Role.

---
**Developed by Nemapu Navaneeth** *5th Semester Computer Science Student | Data Science & ML Enthusiast*
