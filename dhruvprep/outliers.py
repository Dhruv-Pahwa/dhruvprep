import pandas as pd

def remove_outliers_iqr(df):
    df_copy = df.copy()
    
    for col in df_copy.select_dtypes(include=['int64', 'float64']).columns:
        Q1 = df_copy[col].quantile(0.25)
        Q3 = df_copy[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df_copy = df_copy[(df_copy[col] >= lower) & (df_copy[col] <= upper)]
        
    return df_copy