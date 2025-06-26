# 💧 Water Quality Parameter Evaluation and Prediction

**Shell-Edunet Skills4Future 4-Week Internship Program**
**Weeks 1 & 2 Combined Tasks**

---

## 📌 Objective

This project focuses on analyzing and predicting water quality data across multiple stations over the years 2000 to 2021.
Goals:

* Evaluate if water parameters are within acceptable environmental limits
* Classify water quality of samples
* Visualize pollutant trends
* Predict future pollutant levels using machine learning

---

## 📁 Dataset Overview

* **File Used**: `WaterQualityPrediction-Dataset.csv`
* **Records**: 2861 rows
* **Attributes**: 11 columns
* **Time Range**: 2000–2021
* **Preprocessing**: Null rows removed

---

## 🧪 Water Parameters

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

## ✅ Week 1: Data Analysis and Classification

### 🔧 Steps Performed

1. **Data Cleaning**

   * Parsed and sorted by date
   * Dropped rows with null values

2. **Status Labeling**

   * Each parameter tagged as `Acceptable`, `High`, or `Low`

3. **Violation Count**

   * Counted limit violations across all samples
   * Bar chart visualized frequency

4. **Time-Series Visualization**

   * Plotted parameter trends over time
   * Limit lines highlighted violations

5. **Water Quality Classification**

   * Based on number of violations per sample:

     * `Good`: 0 violations
     * `Moderate`: 1–2 violations
     * `Poor`: 3+ violations

6. **Monthly Trend Analysis**

   * Monthly average values plotted for NH₄, BSK5, NO₃, and Cl⁻

### 📦 Outputs

* `WaterQualityPrediction-Processed.csv`: Status flags & quality class
* Charts:

  * Parameter violation counts
  * Time-series plots
  * Monthly average trends
  * Classification distribution

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

### 🧪 Pollutants Predicted

| Parameter | Description      |
| --------- | ---------------- |
| O₂        | Dissolved Oxygen |
| NO₃       | Nitrate          |
| NO₂       | Nitrite          |
| SO₄       | Sulfate          |
| PO₄       | Phosphate        |
| Cl⁻       | Chloride         |

### 📊 Example Output

**Predicted pollutant levels for station `22` in `2024`:**

```
  O2: 6.13
  NO3: 1.89
  NO2: 0.04
  SO4: 70.11
  PO4: 0.03
  CL: 113.25
```

---

## 💾 Files Generated

| File Name                              | Description                       |
| -------------------------------------- | --------------------------------- |
| `WaterQualityPrediction-Processed.csv` | Cleaned and labeled dataset       |
| `pollution_model.pkl`                  | Trained Random Forest model       |
| `model_columns.pkl`                    | Feature structure for predictions |

---

## 🔮 Future Scope

* Use ML models to classify water quality (Good/Moderate/Poor)
* Add seasonal or monthly forecasting granularity
* Apply anomaly detection for unusual pollutant patterns
* Build an interactive dashboard using Dash or Streamlit
