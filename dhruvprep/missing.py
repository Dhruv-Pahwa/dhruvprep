import pandas as pd

def handle_missing(df, strategy="mean"):
    df_copy = df.copy()
    
    for col in df_copy.columns:
        if df_copy[col].isnull().sum() > 0:
            if strategy == "mean" and df_copy[col].dtype != "object":
                df_copy[col].fillna(df_copy[col].mean(), inplace=True)
            elif strategy == "median" and df_copy[col].dtype != "object":
                df_copy[col].fillna(df_copy[col].median(), inplace=True)
            elif strategy == "mode":
                df_copy[col].fillna(df_copy[col].mode()[0], inplace=True)
            elif strategy == "drop":
                df_copy.dropna(inplace=True)
    return df_copy