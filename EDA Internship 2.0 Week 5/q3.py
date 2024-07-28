import pandas as pd

df = pd.read_csv("instagram data.csv", encoding='latin1')
print("\nMissing Values Check:")
print(df.isnull().sum())