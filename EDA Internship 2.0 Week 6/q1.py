import pandas as pd

df = pd.read_csv("births.csv")
df['year'] = df['year'].astype(str)
df['Decade'] = df['year'].str[:3] + '0'
print(df)


