def basic_summary(df):
    return {
        "shape": df.shape,
        "missing_values": df.isnull().sum(),
        "describe": df.describe()
    }