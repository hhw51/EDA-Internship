import pandas as pd

df = pd.read_csv("births.csv", delimiter=',')
print(df.columns)
births_by_month = df.groupby('month')['births'].sum()
births_by_day = df.groupby('day')['births'].sum()
print("Total births by month:")
print(births_by_month)
print("\nTotal births by day:")
print(births_by_day)
