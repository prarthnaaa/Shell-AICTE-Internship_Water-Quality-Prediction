# 💧 Water Quality Parameter Evaluation and Prediction

**Shell-Edunet Skills4Future 4-Week Internship Program**
**By: Prarthna Puhan**

---

## 📌 Objective

This project focuses on analyzing and predicting water quality parameters across multiple stations over the years **1995 to 2050**. The main goals include:

* Checking if pollutant levels are within environmental limits
* Classifying water quality into Good, Moderate, or Poor
* Forecasting future pollutant levels using machine learning models
* Visualizing pollution trends with an interactive app

---

## 📁 Dataset Overview

* **Raw File**: `WaterQualityPrediction-Dataset.csv`
* **Processed File**: `WaterQualityPrediction-Processed.csv`
* **Records**: 2861 rows
* **Time Range**: 2000–2021
* **Columns**: 11 (includes station ID, date, pollutants)
* **Preprocessing**:

  * Missing values were dropped (Week 2)
  * Derived `year` and `month` for feature engineering

---

## 🔍 Water Parameters and Limits

| Parameter | Description                     | Acceptable Limit |
| --------- | ------------------------------- | ---------------- |
| NH₄       | Ammonium                        | < 0.5 mg/L       |
| BSK5      | Biological Oxygen Demand (BOD₅) | < 3 mg/L         |
| Suspended | Suspended Solids                | < 25 mg/L        |
| O₂        | Dissolved Oxygen                | > 5 mg/L         |
| NO₃       | Nitrate                         | < 10 mg/L        |
| NO₂       | Nitrite                         | < 0.1 mg/L       |
| SO₄       | Sulfate                         | < 250 mg/L       |
| PO₄       | Phosphate                       | < 0.1 mg/L       |
| Cl⁻       | Chloride                        | < 250 mg/L       |

---

## ✅ Week 1: Data Cleaning and Classification

### 🔧 Key Steps:

* Sorted by date and dropped rows with null values
* Added `Status` column per pollutant (Acceptable/High/Low)
* Assigned overall **Water Quality Class** based on number of violations:

  * Good = 0 violations
  * Moderate = 1–2 violations
  * Poor = 3+ violations
* Plotted pollutant trends and violation distribution

---

## 🤖 Week 2: Pollutant Level Prediction (ML Model)

### 📌 Objective

Build a machine learning model to predict future concentrations of key pollutants using historical patterns.

### 🛠 Steps Performed

1. **Preprocessing**

   * Converted `date` to datetime
   * Extracted `year` and `month`
   * Dropped rows with missing pollutant values

2. **Feature Engineering**

   * Input: `station id`, `year`
   * Output: pollutant concentrations
   * Encoded station ID using one-hot encoding

3. **Model Training**

   * Model: `RandomForestRegressor` (wrapped in `MultiOutputRegressor`)
   * Split: 80% training, 20% testing

4. **Model Evaluation**

   * Metrics: Mean Squared Error (MSE), R² Score
   * Assessed per pollutant

5. **Future Prediction**

   * Predicted pollutant levels for a given station and year
   * Example: Predicted values for station `22` in `2024`

6. **Model Saving**

   * Model saved as `pollution_model.pkl`
   * Feature structure saved as `model_columns.pkl`

---

## 💾 Week 3: Final Submission (Stacked Ensemble + Streamlit App)

### 🔀 Final Approach: **Stacking Regressor**

* Combined multiple base regressors to improve prediction consistency across pollutants
* Base learners: Random Forest, Gradient Boosting, Linear Regression
* Meta-model: **RidgeCV**
* Built using Streamlit (`Prediction_App.py`)

### 🔗 Inputs:

* `Station ID`
* `Year` (Prediction Range: **1995 to 2050**)

### 🧪 Output:

* Predicted values for 9 pollutants
* Status classification based on environmental thresholds
* Visual summary in the form of a bar chart

---

## 📊 Model Comparison Summary (R² Scores for NH₄–Cl⁻)

| Model             | Avg R² Score | Notes                                  |
| ----------------- | ------------ | -------------------------------------- |
| Random Forest     | Moderate     | Strong for NH₄, Cl⁻; weak for NO₂      |
| Gradient Boosting | Moderate     | Good for NH₄, PO₄                      |
| Linear Regression | Moderate     | Very good for SO₄, Cl⁻                 |
| XGBoost           | Moderate     | Balanced but low on NO₂                |
| LightGBM          | Moderate     | Strong on SO₄, Cl⁻                     |
| Neural Network    | Low          | Poor performance overall               |
| **Stacking**      | **Best**     | Most consistent overall across metrics |

---

## 🗂️ Files Included

| File Name                              | Description                               |
| -------------------------------------- | ----------------------------------------- |
| `Final-Week_3.ipynb`                   | Final model training + evaluation         |
| `Prediction_App.py`                    | Streamlit app to predict pollution levels |
| `WaterQualityPrediction-Processed.csv` | Cleaned dataset with quality labels       |
| `Week_1.ipynb`                         | Data cleaning, analysis, and labeling     |
| `Week_2.ipynb`                         | Initial ML model and evaluations          |
| `PrarthnaPuhan-Project_PPT.pptx`       | Final presentation slides                 |

---

## 🔮 Future Scope

* Use classification models to directly predict `Good/Moderate/Poor`
* Add spatial and seasonal factors to improve prediction
* Visualize results in an interactive dashboard
* Use anomaly detection to catch outliers in water quality
