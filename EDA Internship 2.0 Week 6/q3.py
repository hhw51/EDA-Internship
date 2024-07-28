import pandas as pd

df = pd.read_csv("births.csv")
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)
