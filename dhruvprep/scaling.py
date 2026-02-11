from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def standard_scale(df, columns):
    df_copy = df.copy()
    scaler = StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy


def minmax_scale(df, columns):
    df_copy = df.copy()
    scaler = MinMaxScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy