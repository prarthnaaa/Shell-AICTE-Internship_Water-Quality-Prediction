# 💧 Water Quality Analysis

**Project Title:** Water Quality Parameter Evaluation and Trend Analysis
**Internship:** Week 1 Assignment – *Shell-Edunet Skills4Future 4-week Internship Program*

---

## 📌 Objective

This project analyzes water quality data to:

* Check if each parameter is within acceptable environmental limits
* Count and visualize parameter violations
* Classify overall water quality of each sample
* Identify monthly pollutant trends

---

## 📁 Dataset

* **File:** `WaterQualityPrediction-Dataset.csv`
* **Rows:** 2861
* **Columns:** 11
* **Date Range:** 2000 to 2021
* **Note:** Rows with missing (null) values were removed during preprocessing.

### Key Parameters:

| Parameter | Description                     |
| --------- | ------------------------------- |
| NH₄       | Ammonium                        |
| BSK5      | Biological Oxygen Demand (BOD₅) |
| Suspended | Suspended Solids                |
| O₂        | Dissolved Oxygen                |
| NO₃       | Nitrate                         |
| NO₂       | Nitrite                         |
| SO₄       | Sulfate                         |
| PO₄       | Phosphate                       |
| Cl⁻       | Chloride                        |

---

## ⚙️ Steps Performed

### 1. Data Cleaning

* Parsed the `date` column
* Sorted entries chronologically
* **Dropped rows with null values**

### 2. Parameter Status Classification

Each parameter was compared against environmental limits:

| Parameter | Threshold Condition |
| --------- | ------------------- |
| NH₄       | < 0.5 mg/L          |
| BSK5      | < 3 mg/L            |
| Suspended | < 25 mg/L           |
| O₂        | > 5 mg/L            |
| NO₃       | < 10 mg/L           |
| NO₂       | < 0.1 mg/L          |
| SO₄       | < 250 mg/L          |
| PO₄       | < 0.1 mg/L          |
| Cl⁻       | < 250 mg/L          |

Each value was labeled as **"Acceptable"**, **"High"**, or **"Low"**.

### 3. Violation Count

* Counted how often each parameter exceeded its acceptable limit
* Bar chart visualized violations across all samples

### 4. Time-Series Trend Analysis

* Plotted concentration levels over time for each parameter
* Limit lines shown to highlight violations clearly

### 5. Water Quality Classification

Samples were classified based on total violations:

* **Good:** 0 violations
* **Moderate:** 1–2 violations
* **Poor:** 3 or more violations

### 6. Monthly Trend Analysis

* Monthly average values calculated for NH₄, BSK5, NO₃, and Cl⁻
* Line chart revealed seasonal variation in water quality

---

## 📦 Outputs

* ✅ `WaterQualityPrediction-Processed.csv`: Final dataset with status flags and quality class
* 📊 Visualizations:

  * Count of parameter violations
  * Time-series plots of all parameters
  * Water quality classification distribution
  * Monthly average trends

---

## 🧠 Future Extensions

* Use ML models to predict future water quality categories
* Detect anomalies using unsupervised learning
* Create an interactive dashboard using Plotly/Dash"# Shell-AICTE-Internship_Water-Quality-Prediction" 
