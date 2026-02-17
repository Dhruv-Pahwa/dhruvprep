# DhruvPrep
> A Lightweight Data Preprocessing Toolkit for Machine Learning

DhruvPrep is a modular Python library designed to simplify data preprocessing for structured machine learning workflows. It provides reusable utilities for:

- Handling missing values
- Detecting multicollinearity (VIF & correlation)
- Removing outliers using IQR
- Encoding categorical variables
- Scaling numerical features
- Generating basic EDA summaries

DhruvPrep helps standardize and automate repetitive preprocessing steps, making datasets ready for model training.

---

## 📦 Installation
```bash
pip install dhruvprep
```

---

## 🧪 Usage

### Import
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
```

### Missing Values
```python
df = handle_missing(df, strategy="mean")
```

### Outlier Removal
```python
df = remove_outliers_iqr(df)
```

### Multicollinearity Detection
```python
# VIF
vif = calculate_vif(df.select_dtypes(include=["int64", "float64"]))
print(vif)

# High correlation
high_corr_cols = high_correlation(df, threshold=0.9)
print("Highly correlated columns:", high_corr_cols)
```

### Encoding
```python
df = label_encode(df, columns=["Gender"])
df = one_hot_encode(df, columns=["City"])
```

### Scaling
```python
df = standard_scale(df, columns=["Age", "Salary"])
df = minmax_scale(df, columns=["Age", "Salary"])
```

### EDA Summary
```python
summary = basic_summary(df)
print(summary["shape"])
print(summary["missing_values"])
print(summary["describe"])
```
