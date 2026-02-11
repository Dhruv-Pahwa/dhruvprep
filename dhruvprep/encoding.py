import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encode(df, columns):
    df_copy = df.copy()
    le = LabelEncoder()
    
    for col in columns:
        df_copy[col] = le.fit_transform(df_copy[col])
        
    return df_copy


def one_hot_encode(df, columns):
    return pd.get_dummies(df, columns=columns)