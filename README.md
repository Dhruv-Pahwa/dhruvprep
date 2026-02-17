# DhruvPrep 
*A Lightweight Data Preprocessing Toolkit for Machine Learning*

DhruvPrep is a modular Python library designed to simplify 
data preprocessing for structured machine learning workflows.

It provides reusable utilities for:

- Handling missing values
- Detecting multicollinearity (VIF & correlation)
- Removing outliers using IQR
- Encoding categorical variables
- Scaling numerical features
- Generating basic EDA summaries

DhruvPrep helps standardize and automate repetitive preprocessing steps, making datasets ready for model training.

---

## 🧪 Example: How to Use DhruvPrep

### 🔹 Full Feature Demonstration

```python
from dhruvprep import (
    handle_missing,
    remove_outliers_iqr,
    calculate_vif,
    high_correlation,
    label_encode,
    one_hot_encode,
    standard_scale,
    minmax_scale,
    basic_summary
)

# Handle missing values
df = handle_missing(df, strategy="mean")

# Remove outliers
df = remove_outliers_iqr(df)

# VIF calculation
vif = calculate_vif(df.select_dtypes(include=["int64", "float64"]))
print(vif)

# High correlation detection
high_corr_cols = high_correlation(df, threshold=0.9)
print("Highly correlated columns:", high_corr_cols)

# Encoding
df = label_encode(df, columns=["Gender"])
df = one_hot_encode(df, columns=["City"])

# Scaling
df = standard_scale(df, columns=["Age", "Salary"])
df = minmax_scale(df, columns=["Age", "Salary"])

# Basic EDA Summary
summary = basic_summary(df)

print(summary["shape"])
print(summary["missing_values"])
print(summary["describe"])

---

## 📦 Installation

### Install from PyPI

```bash
pip install dhruvprep
